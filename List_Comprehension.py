import os

os.system('cls')

#Example for writing a list till 99 the normal way 
my_list = []
for num in range(0,100):
    my_list.append(num)

print(my_list)

#Example for writing a list till 99 by using list comprehnsion as u can see its much for effective
my_list_comp = [num for num in range(0,100)]

print(my_list_comp)

#Example for using if comands in a list comphrehension  as u can see it stops at 19
my_list_comp_if = [num for num in range(0,100) if num < 20]

print(my_list_comp_if)

#Example for filtering the numbers in the list less then 25
inventory_name = ['Screws', 'Wheels', 'Metal Parts', 'Ruber Bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

#To combine our lists together
replenish_list = [(name,number) for name, number in zip(inventory_name, inventory_numbers) if number < 25]

print(replenish_list)

