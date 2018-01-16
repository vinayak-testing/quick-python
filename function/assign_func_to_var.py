"""Demonstrate how functions can be assigned to variables like other python objects"""


def f_to_kelvin(degree_f):
    return 273.15 + (degree_f - 32) * 5 / 9


def c_to_kelvin(degree_c):
    return 273.15 + degree_c


abs_temp = f_to_kelvin
print(abs_temp(32))

abs_temp = f_to_kelvin
print(abs_temp(42))


t = {'Ftok': f_to_kelvin, 'Ctok': c_to_kelvin}

print(t['Ftok'](32))

print(t['Ctok'](400))
