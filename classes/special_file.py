"""To Demonstrate the destruction of objects and release of memory"""


class SpecialFile:

    def __init__(self):
        self.__file = open('special.txt', 'w')
        self.__file.write('****** Start Special File ****** \n\n')

    def write(self, str):
        self.__file.write(str)
        self.__file.write("\n")

    def close(self):
        print(self.__file)
        self.__file.close();

    def __del__(self):
        print("Entered __del___")
        self.close()


def test():
    f = SpecialFile()
    f.write("Writing the first line")
    f.close()
    f.close()
    # print(f.__file)


test()
