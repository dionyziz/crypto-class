from exercises.registry import register_grader

def validate(metadata, input_pass):
    '''
    Check if password in metadata and user input match.
    '''
    return metadata['password'] == input_pass

register_grader('1.1', validate)
register_grader('1.2', validate)
register_grader('1.3', validate)
