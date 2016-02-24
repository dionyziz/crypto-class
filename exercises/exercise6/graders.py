# -*- coding: utf-8 -*-

import re, sys, gnupg

from bs4 import BeautifulSoup
from urllib2 import urlopen

from exercises.registry import register_grader

PGP_MIT_KEYSERVER = 'pgp.mit.edu'
gpg = gnupg.GPG()

def print_info(decrypted):
    print('User name: %s' % decrypted.username)
    print('Key id: %s' % decrypted.key_id)
    print('Signature id: %s' % decrypted.signature_id)
    print('Signature timestamp: %s' % decrypted.sig_timestamp)
    print('Fingerprint: %s' % decrypted.fingerprint)

def hasStudentEmail(verified, student_email):
    emailList = re.findall(r"(?<=\<).+(?=\>)", unicode(verified.username))
    return student_email in emailList

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def hasAtLeastOneSignature(verified, student_email):
    page = urlopen('http://pgp.mit.edu/pks/lookup?op=vindex&search=0x' + verified.key_id)
    html = page.read()

    soup = BeautifulSoup(html)
    a_text = [tag.text for tag in soup.find_all('a') if tag.text]

    # Find all email addresses
    emails = [ ]
    for text in a_text:
        match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        if len(match) > 0 and (student_email not in match):
            emails += match

    return len(emails) > 0


# Assumes lookupMIT works, otherwise I can't fetch the pub key
def hasExpirationDate(verified):
    result = gpg.search_keys(verified.key_id, PGP_MIT_KEYSERVER)
    return len(result) > 0 and len(result[0]['expires']) > 0

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def has4096Length(verified):
    result = gpg.search_keys(verified.key_id, PGP_MIT_KEYSERVER)
    return len(result) > 0 and result[0]['length'] == '4096'

# Looks up the key id in pgp.mit.edu
def lookupMIT(verified):
    result = gpg.search_keys(verified.key_id, PGP_MIT_KEYSERVER)
    return len(result) > 0

# Imports public key to local keyring
# Assumes lookupMIT works, otherwise I can't fetch the pub key
def importKeyFromData(signed_data):
    verified = gpg.verify(signed_data)
    if not verified.key_id:
        return
    result = gpg.recv_keys(PGP_MIT_KEYSERVER, verified.key_id)


def validate(metadata, signed_data):
    importKeyFromData(signed_data)
    verified = gpg.verify(signed_data)

    # Check is msg was signed. If not, there's no point to continue
    if not verified.key_id:
        return False, u'Το κείμενο δεν ειναι υπογεγραμμένο με έγκυρο GPG κλειδί.'

    lookedup = lookupMIT(verified)
    if not lookedup:
        return False, u'Το κλειδί σου δεν βρέθηκε στον MIT keyserver. Παρακαλούμε ανέβασε το κλειδί σου και ξαναπροσπάθησε.'

    hasEmail = hasStudentEmail(verified, metadata['user_email'])
    if not hasEmail:
        return False, u'Το κλειδί που χρησιμοποιήθηκε για την υπογραφή (%s) δεν ειναι το ίδιο με το email που δήλωσες στο crypto-class.gr (%s).' % (
                            verified.username,
                            metadata['user_email'],
                            )

    oneSignature = hasAtLeastOneSignature(verified, metadata['user_email'])
    if not oneSignature:
        return False, u'Το κλειδί σου δεν έχει λάβει καμία υπογραφή. Λάβε μια υπογραφή, απο εναν συμφοιτητή σου, και ξαναπροσπάθησε.'

    hasExpiration = hasExpirationDate(verified)
    if not hasExpiration:
        return False, u'Στο κλειδί σου δεν έχει οριστεί ημερομηνία λήξης. Παρακαλούμε ξαναδημιούργησε το κλειδί σου και ξαναπροσπάθησε.'

    has4096 = has4096Length(verified)
    if not has4096:
        return False, u'Το κλειδί σου δεν έχει μήκος 4096 bits. Παρακαλούμε ξαναδημιούργησε το κλειδί σου και ξαναπροσπάθησε.'

    # Solution is correct!
    return True

register_grader('20.1', validate)
