"""Functions are first class objects in python, i.e they can be passed around as
variables across the language. This allows to implement a more consice decorator pattern
."""


def decorate(func):
    print("Inside decorator() decorating ", func.__name__)

    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)

    return wrapper_func


@decorate
def myfunction(parameters):
    """

    :param parameters:
    """
    print(parameters)


@decorate
def myfunction2(parameters):
    """

    :param parameters:
    """
    print(parameters)


# myFunction = decorate(myFunction)
myfunction('Hello')
myfunction2('Hello')
