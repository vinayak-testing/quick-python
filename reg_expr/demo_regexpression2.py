"""Module to demonstrate the extraction of values from
regular expression. Defined reg exp should parse the below example line
Example: lastname, firstname middlename:phonennumber
            phonenumber is of format: 999-999-9999"""

import re

reg_exp = re.compile(r"(?P<last>[-a-zA-Z]+),"     #lastname,
                     r" (?P<first>[-a-zA-Z]+)"     # firstname
                     r"( (?P<middle>[-a-zA-Z]+))?"  # [middlename]
                     r": (?P<phone>(\d{3}-)?\d{3}-\d{4})") #: [999-]999-9999

with open('telephone.txt') as file:
    for line in file.readlines():
        result = reg_exp.search(line)
        if result is None:
            print("Oops, Record is not of correct format")
        else:
            first_name = result.group('first')
            last_name = result.group('last')
            middle_name = result.group('middle')
            phone = result.group('phone')

            print("Name:", first_name, middle_name, last_name, " phonenumber: ", phone)




