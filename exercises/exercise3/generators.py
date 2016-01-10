import random
from .models import RSAValues
from exercises.registry import register_generator

class RSAWienerExercise(object):
    def __init__(self, args_dict=None):
        if len(args_dict) == 1:
            args_dict = {}
        try:
            if 'metadata' in args_dict:
                self.metadata = args_dict['metadata']
                self.message = self.metadata['message']
            else:
                self.metadata = { }
                rsa_value = random.choice(RSAValues.objects.all())

                message = 'n:\n' + rsa_value.n + '\n\ne:\n' + rsa_value.e
                self.metadata['message'] = self.message = message
                self.metadata['private-key'] = rsa_value.d
        except Exception, e:
            print e.message
            exit(1)

register_generator('14.0', RSAWienerExercise)
