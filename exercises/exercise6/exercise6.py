import sys,gnupg,re,subprocess
import os.path

gpg = gnupg.GPG()

def get_emails(emailString):
    emailList = re.findall(r"(?<=\<).+(?=\>)", str(emailString))
    return emailList

def print_info(decrypted):
    print('User name: %s' % decrypted.username)
    print('Key id: %s' % decrypted.key_id)
    print('Signature id: %s' % decrypted.signature_id)
    print('Signature timestamp: %s' % decrypted.sig_timestamp)
    print('Fingerprint: %s' % decrypted.fingerprint)

def hasStudentEmail(verified):
    # XXX: Get studentEmail from some DB
    studentEmail = "elefthei@Lefs-MacBook-Air.local"
    emailList = get_emails(verified.username)
    return studentEmail == emailList[0]

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

def main():
    if(len(sys.argv)) != 2 or not os.path.isfile(sys.argv[1]):
        print "Usage: pgpg <SIGNED FILE>"

    stream = open(sys.argv[1], "rb")

    ### DEBUG: Sign file on the fly for testing ####
    # signed_data = gpg.sign_file(stream)

    verified = gpg.verify_file(stream)
    lookedup = lookupMIT(verified) 
    hasStudentEmail = hasStudentEmail(verified)
    oneSignature = hasAtLeastOneSignature(verified)
    hasExpiration = hasExpirationDate(verified)
    has4096 = has4096Length(verified)

    print "Verify Signature: OK" if verified else "Verify Signature: ERROR"
    print "Look-Up Server MIT: OK" if lookedup else "Look-UP MIT Server: ERROR"
    print "Has NTUA Student Email: OK" if hasStudentEmail else "Has NTUA Student Email: ERROR"
    print "Has at least one Signature: OK" if oneSignature else "Has at least one Signature: ERROR"
    print "Has Expiration Date: OK" if hasExpiration else "Has Expiration Date: ERROR"
    print "Has length of 4096: OK" if has4096 else "Has length of 4096: ERROR"

    # print_info(verified)

if __name__ == "__main__":
    main()


