""" halt problem https://en.wikipedia.org/wiki/Halting_problem"""
import inspect

DATA = {}

# 0 undefined for now
# 1 finish
# 2 no finish


def halts(x, arg):
    """halt function check if a function halt or not"""
    if callable(x):
        # is a function
        name = x.__name__
        if (name, arg) in DATA:
            # we already know the result
            if DATA[(name, arg)] == 0:
                # undefined
                DATA[(name, arg)] = 2
                return False
            elif DATA[(name, arg)] == 1:
                # finish
                return True
            elif DATA[(name, arg)] == 2:
                # no finish
                return False
        else:
            DATA[(name, arg)] = 0
        _source_code = inspect.getsource(x)
        # here we need to check that the function is omnipotent
        x(arg)
        if DATA[(name, arg)] == 0:
            DATA[(name, arg)] = 1
            return True
    else:
        # not a function, we don't care so True
        return True
    if DATA[(name, arg)] == 1:
        return True
    else:
        return False


def g(x):
    """proof function"""
    if halts(x, x):
        # loop forever
        while True:
            pass


if __name__ == "__main__":
    RESULT = halts(g, g)
    print(f"function {g.__name__} halt: {RESULT}")
