"""Demonstrate construction of lamda function"""
funs = {'FtoK': lambda f_deg: 273.15 + (f_deg - 32) * 5 / 9,
        'CtoK': lambda c_deg: 273.15 + c_deg}


print(funs['FtoK'](40))
print(funs['CtoK'](400))
