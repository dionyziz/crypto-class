import string
import random
import hashlib
from exercises.registry import register_generator

def password_generator(length=6):
    '''
    Create a random string of lowercase letters.
    '''
    return 'the_password_is_' + ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(length))

class HashExercise(object):
    '''
    SHA256 encoding class for the hands-on exercise of lesson 6 of crypto-class.
    '''
    def __init__(self, arg_dict=None):
        self.metadata = {}
        self.metadata['password'] = password_generator()
        self.encode()

    def encode(self):
        self.metadata['message'] = self.message = hashlib.sha256(self.metadata['password'].encode('utf8')).hexdigest()

register_generator('6.0', HashExercise)
