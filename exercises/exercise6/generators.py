from exercises.registry import register_generator

class PGPExercise(object):
    '''
    Hands-on exercise for PGP signing a file
    '''
    def __init__(self, args_dict=None):
        if 'user' not in args_dict:
            print 'User is required for PGP exercise initialization'
            exit(1)

        user = args_dict['user']

        if not user.is_authenticated():
            self.message = 'email@example.com'
            self.metadata = { }
            return

        # user is authenticated
        self.metadata = {
            'user_email': user.email
        }
        self.message = user.email

register_generator('20.1', PGPExercise)
