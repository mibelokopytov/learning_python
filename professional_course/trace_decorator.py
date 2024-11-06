import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(res)}')
        return res
    return wrapper