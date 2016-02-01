from exercises.registry import register_grader


def validate(metadata, input_pass):
    '''
    Check if password in metadata and user input match.
    '''
    is_solution = metadata['password'] == input_pass
    return (is_solution, None)

register_grader('18.0', validate)
