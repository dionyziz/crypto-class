import re, sys, gnupg
from exercises.registry import register_grader

gpg = gnupg.GPG()

def print_info(decrypted):
    print('User name: %s' % decrypted.username)
    print('Key id: %s' % decrypted.key_id)
    print('Signature id: %s' % decrypted.signature_id)
    print('Signature timestamp: %s' % decrypted.sig_timestamp)
    print('Fingerprint: %s' % decrypted.fingerprint)

def hasStudentEmail(verified, student_email):
    emailList = re.findall(r"(?<=\<).+(?=\>)", str(verified.username))
    return student_email in emailList

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def hasAtLeastOneSignature(verified):
    result = gpg.recv_keys('pgp.mit.edu', verified.key_id)
    return result.n_sigs > 0

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def hasExpirationDate(verified):
    result = gpg.search_keys(verified.key_id, 'pgp.mit.edu')
    return len(result) > 0 and result[0]['expires']

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def has4096Length(verified):
    result = gpg.search_keys(verified.key_id, 'pgp.mit.edu')
    return len(result) > 0 and result[0]['length'] == '4096'

# Looks up the key id in pgp.mit.edu
def lookupMIT(verified):
    result = gpg.search_keys(verified.key_id, 'pgp.mit.edu')
    return len(result) > 0

def validate(metadata, signed_data):

    verified = gpg.verify(signed_data)
    lookedup = lookupMIT(verified) 
    hasStudentEmail = hasStudentEmail(verified, metadata['user_email'])
    oneSignature = hasAtLeastOneSignature(verified)
    hasExpiration = hasExpirationDate(verified)
    has4096 = has4096Length(verified)

    # print_info(verified)
    return verified and lookedup and hasStudentEmail and oneSignature and hasExpiration and has4096

register_grader('20.0', validate)

