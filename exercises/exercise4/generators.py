from exercises.registry import register_generator

class OnionExercise(object):
    '''
    Hands-on exercise for creating an onion address
    '''
    def __init__(self, args_dict=None):
        if 'user' not in args_dict:
            print 'User is required for OnionExercise initialization'
            exit(1)

        user = args_dict['user']
        self.metadata = {
            'user_email': user.email
        }
        self.message = user.email

register_generator('20.0', OnionExercise)
