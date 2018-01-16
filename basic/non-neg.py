from itertools import count
from tkinter import font

x = [1, 3, 5, 0, -1, 3, -2]

for i in x:
    if i < 0:
        x.remove(i)
print(x)


y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]

z = []
count = 0
for j in y:
    z = z + j

for k in z:
    if k < 0:
        count += 1
print(z)
print(count)
