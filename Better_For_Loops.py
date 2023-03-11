import os

#To clear the terminal before running
os.system('cls')

#List of items you have
inventory_name = ['Screws', 'Wheels', 'Metal Parts', 'Ruber Bits', 'Screwdrivers', 'Wood']

#List of amount of items you have
inventory_numbers = [43, 12, 95, 421, 23, 43]

#We want to use a for loop on these codes and connect it but we cant as for loops will only work for one list
#The zip zips the code into a number you will see while running the code and its not that usefull so we will make it 
#into a list if you take out the list in the code it will print a number which is useless for us in this case

#And now we add the print name and number to it so it looks a bit better and easier to read and also add a f string
for name, number in (zip(inventory_name,inventory_numbers)):
    print(f'{name} current inventory: {number}')

print(zip(inventory_name,inventory_numbers))