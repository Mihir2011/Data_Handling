import os

os.system('cls')

#Basic sorting example for small to big
list_1 = [4,2,3,1,5]
print(sorted(list_1))

#Basic sorting example for big to small
list_2 = [4,2,3,1,5]
print(sorted(list_2, reverse = True))

#Complex sorting example normally and by using lambda functions
list_3 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]
def sort_function(item):
    return item[1]
print(sorted(list_3, key = sort_function))
print(sorted(list_3, key = lambda item: item[1]))