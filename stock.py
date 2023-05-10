from file_handling import read_laptop_inventory, update_laptop_inventory
from tabulate import tabulate

def list_laptops():
    print("List of Available Laptops")
    # Load the inventory from file
    inventory = read_laptop_inventory('inventory.txt')
    
    # create a list of index values
    index = [i+1 for i in range(len(inventory))]
    
    # print the array in a table design
    print(tabulate(inventory, headers="keys", showindex=index, tablefmt="fancy_grid"))