# with open('infile', 'r') as file_obj:
#     line = file_obj.readline()
#     print(line.strip('\n'))
#
#


from pathlib import Path

p_text = Path('my_text')
x = p_text.write_bytes(b'THis is binary data')
print(x)
y = p_text.read_text()
print(y)

x = input('Enter the file name to use:')
print(x)