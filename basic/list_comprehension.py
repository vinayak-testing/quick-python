x = [1, 2, 3, 4]

x_squared = [item*item for item in x if item > 2]

print(x_squared)

x_squared_dict = {item: item*item for item in x if item > 2}

print(x_squared_dict)
