import functools


def prefix(string, to_the_end = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            else:
                return string + func(*args, **kwargs)
        return wrapper
    return decorator