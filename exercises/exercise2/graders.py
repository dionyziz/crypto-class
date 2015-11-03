from exercises.registry import register_grader

def validate(metadata, input_pass):
    '''
    Check if password in metadata and user input match.
    '''
    return True if metadata['password'] == input_pass else False

register_grader('6.0', validate)
