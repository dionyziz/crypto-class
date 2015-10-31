import base64
import string
import random
from .models import Base64Quote, Rot13Quote, SubstitutionQuote
from exercises.registry import register_generator

def password_generator(length=10):
    '''
    Create a random string of uppercase letters.
    '''
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(length))


class Base64Exercise(object):
    '''
    base64 encoding and decoding functions for the first hands-on exercise of crypto-class.
    '''
    def __init__(self, args_dict = None):
        if args_dict is None:
            args_dict = {}
        try:
            if 'metadata' in args_dict:
                self.metadata = args_dict['metadata']
                self.message = self.metadata['message']
                self.decode()
            else:
                self.metadata = {}
                quote = random.choice(Base64Quote.objects.all()).quote
                self.metadata['password'] = password_generator()
                self.metadata['cleartext'] = quote + '\nPassword ' + self.metadata['password']
                self.encode()
                self.decode()
        except KeyError:
            print 'base64: Invalid argument dictionary structure.'
            exit(1)

    def encode(self):
        self.metadata['message'] = self.message = base64.b64encode(self.metadata['cleartext'])

    def decode(self):
        self.cleartext = base64.decodestring(self.message)

class Rot13Exercise(object):
    '''
    rot13 encoding and decoding functions for the first hands-on exercise of crypto-class.
    '''
    def __init__(self, args_dict = None):
        if args_dict is None:
            args_dict = {}
        try:
            if 'metadata' in args_dict:
                self.metadata = args_dict['metadata']
                self.message = self.metadata['message']
                self.encode('d')
            else:
                self.metadata = {}
                quote = random.choice(Rot13Quote.objects.all()).quote
                self.metadata['password'] = password_generator()
                self.metadata['cleartext'] = quote + '\nPassword '+ self.metadata['password']
                self.encode('e')
        except KeyError:
            print 'rot13: Invalid argument dictionary structure.'
            exit(1)

    def encode(self, mode):
        out = ''
        inp = self.metadata['cleartext'] if mode == 'e' else self.message
        for char in inp:
            if char not in string.letters:
                out += char
            else:
                if char in string.lowercase:
                    out += string.lowercase[(string.lowercase.index(char) + 13) % len(string.lowercase)]
                else:
                    out += string.uppercase[(string.uppercase.index(char) + 13) % len(string.uppercase)]
        if mode == 'e':
            self.metadata['message'] = self.message = out
        else:
            self.cleartext = out

class SubstitutionExercise(object):
    '''
    Substitution encoding and decoding functions for the first hands-on exercise of crypto-class.
    '''
    def __init__(self, args_dict = None):
        if args_dict is None:
            args_dict = {}
        self.exercise = ''
        if 'metadata' in args_dict:
            self.metadata = args_dict['metadata']
            self.encode('d')
        else:
            self.metadata = {}
            quote = random.choice(SubstitutionQuote.objects.all()).quote
            random_lst = list(string.ascii_uppercase)
            random.shuffle(random_lst)
            self.metadata['permutation'] = ''.join(random_lst)
            self.metadata['password'] = password_generator()
            self.metadata['cleartext'] = quote.upper() + '\nPassword '.upper() + self.metadata['password']
            self.encode('e')

    def encode(self, mode):
        out = ''
        inp = self.metadata['cleartext'] if mode == 'e' else self.message
        for pos, ch in enumerate(inp):
            if ch not in string.uppercase:
                out += ch
            else:
                if mode == 'e':
                    offset = ord(ch) - ord('A')
                    out += self.metadata['permutation'][offset]
                else:
                    offset = self.metadata['permutation'].find(ch)
                    out += string.ascii_uppercase[offset]
        if mode == 'e':
            self.metadata['message'] = self.message = out
        else:
            self.cleartext = out

register_generator('1.1', Base64Exercise)
register_generator('1.2', Rot13Exercise)
register_generator('1.3', SubstitutionExercise)
