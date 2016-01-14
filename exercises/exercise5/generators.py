from django.conf import settings
from exercises.registry import register_generator

from .models import HttpsPassword
import random

class HttpsExercise(object):
    '''
    Hands-on exercise for HTTPS traffic decryption
    '''
    def __init__(self, args_dict=None):
        exercise_packet = random.choice(HttpsPassword.objects.all())
        self.metadata = {
            'password': exercise_packet.password
        }
        self.message = '<a href="%s">Download file</a>' % (settings.MEDIA_URL + exercise_packet.filename)

register_generator('18.0', HttpsExercise)
