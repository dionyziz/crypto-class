from exercises.registry import register_generator

class OnionExercise(object):
    '''
    Hands-on exercise for creating an onion address
    '''

    def __init__(self, user):
        self.metadata = {
            'user': user
        }
        self.message = user.email

register_generator('20.0', OnionExercise)
