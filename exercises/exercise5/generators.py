from .models import HttpsPassword
from exercises.registry import register_generator
import random


class HttpsExercise(object):
    '''
    Hands-on exercise for HTTPS traffic decryption
    '''
    def __init__(self):
        exercise_packet = random.choice(HttpsPassword.objects.all())
        self.metadata = {
            'password': exercise_packet.password
        }
        self.message = exercise_packet.filename

register_generator('18.0', HttpsExercise)
