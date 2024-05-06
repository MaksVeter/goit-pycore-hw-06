from functools import wraps

def input_error_catch(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f"Value Error: {str(error)}"
        except KeyError as error:
            return f"Key Error: {str(error)}"

    return inner


def require_two_args(func):
    @wraps(func)
    def inner(args, contacts):
        if (len(args) != 2):
            raise ValueError('Operation Requires 2 args: name and phone')
        return func(args, contacts)

    return inner


def name_min_length(func):
    @wraps(func)
    def inner(args, contacts):
        if (len(args[0]) <= 3):
            raise ValueError('Name should be more the 3 symbols')
        return func(args, contacts)

    return inner
