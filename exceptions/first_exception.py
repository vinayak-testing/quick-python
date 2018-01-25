"""
Define new custom exception class
"""


class MyError(Exception):
    pass


if __name__ == '__main__':

    try:
        raise MyError("Something went wrong")
    except MyError as e:
        print(e)

    try:
        raise MyError("Some Information", "My_file", 3)
    except MyError as error:
        print("Situation: {0} problem with file {1}: {2}".format
              (error.args[2], error.args[1], error.args[2]))
