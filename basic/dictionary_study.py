print("Enter 3 Names")
age_dict = {}
x = input()
y = input()
z = input()
print("Enter their ages")
age_dict[x] = input()
age_dict[y] = input()
age_dict[z] = input()

name = input("Enter name to find out age :")
print(name, "age is", age_dict[name])