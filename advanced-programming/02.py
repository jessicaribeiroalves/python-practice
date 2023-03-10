
def flat(arg):
    return sum([elem if type(elem) == list else [elem] for elem in arg], [])


def flatten_lists(func):
    def wrapper(*args):
        flat_args = flat(args)
        return func(*flat_args)
    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = [int(x) if type(x) == str and x.lstrip(
            "-").isdigit() else x for x in args]
        return func(*new_args)
    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []
        for x in args:
            if type(x) == int:
                new_args.append(x)
        return func(*new_args)
    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)
