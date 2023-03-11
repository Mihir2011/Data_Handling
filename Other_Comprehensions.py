import os

os.system('cls')

#Example for set comprehension
set_comp = {num for num in range(100)}
print(set_comp)

#Example for dictionary comprehension
dict_comp = {num: num for num in range(100)}
print(dict_comp)

#Example for tuple comprehension
tuple_comp = tuple(num for num in range(100))
print(tuple_comp)