"""Module to demonstrate the composition of regular expression. Defined reg exp should parse the below example line
Example: lastname, firstname middlename:phonennumber
            phonenumber is of format: 999-999-9999"""

import re

reg_exp = re.compile(r"[-a-zA-Z]+,"     #lastname,
                     r" [-a-zA-Z]+"     # firstname
                     r"( [-a-zA-Z]+)?"  # [middlename]
                     r": (\d{3}-)?\d{3}-\d{4}") #: [999-]999-9999

with open('telephone.txt') as file:
    for line in file.readlines():
        if reg_exp.search(line):
            print(line)




