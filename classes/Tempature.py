"""To demonstrate usage of properties in python"""


class Tempature:

    def __init__(self, t=100):
        self._temp_far = t

    @property
    def temp(self):
        return (self._temp_far - 32) * 5 /9

    @temp.setter
    def temp(self, new_temp):
        self._temp_far = new_temp * 9 / 5 + 32


temp = Tempature()
print(temp._temp_far)

temp.temp = 10
print(temp.temp)
print(temp._temp_far)






