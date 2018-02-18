"""
To demonstrate the usage of with key word for the new
for the new concept of context manager introduced in
python3. context managers are relatively new and their
usage will mature with time.

They are meant for below mentioned usages
    - locking and unlocking of resources
    - opening and closing of files
    - committing database changes
"""

with open("../README.md") as infile:
    text = infile.read()
    print(text)
