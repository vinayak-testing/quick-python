"""module to demonstrate basic regular expression capabillty"""

import re

count = 0
regexpr = re.compile("hello")

with open("input.txt") as file:
    for line in file.readlines():
        if regexpr.search(line):
            count += 1


print(count)
