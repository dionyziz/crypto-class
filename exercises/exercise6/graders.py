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
    return len(result) > 0 and len(result[0]['expires']) > 0

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def has4096Length(verified):
    result = gpg.search_keys(verified.key_id, 'pgp.mit.edu')
    return len(result) > 0 and result[0]['length'] == '4096'

# Looks up the key id in pgp.mit.edu
def lookupMIT(verified):
    result = gpg.search_keys(verified.key_id, 'pgp.mit.edu')
    return len(result) > 0

# Assumes lookupMIT works, otherwise I can't fetch the pub key
def importKeyFromData(signed_data):
    verified = gpg.verify(signed_data)
    result = gpg.recv_keys(verified.key_id, 'pgp.mit.edu')
    return

def validate(metadata, signed_data):
    #importKeyFromData(signed_data)
    verified = gpg.verify(signed_data)

    # Check is msg was signed. If not, there's no need to continue!
    if not verified.key_id:
        return False

    lookedup = lookupMIT(verified)
    hasEmail = hasStudentEmail(verified, metadata['user_email'])
    oneSignature = hasAtLeastOneSignature(verified)
    hasExpiration = hasExpirationDate(verified)
    has4096 = has4096Length(verified)

    #print_info(verified)
    is_solution = verified and lookedup and hasEmail and oneSignature and hasExpiration and has4096
    return (is_solution, error_msg)

register_grader('20.1', validate)
