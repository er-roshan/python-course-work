from file_handling import read_laptop_inventory, update_laptop_inventory
from invoice import generate_sale_invoice, write_sell_invoice_to_file
from stock import list_laptops

def sell_laptop():
    
    inventory = read_laptop_inventory('inventory.txt')
    list_laptops()
    
    # Sell a laptop
    laptop_index = int(input("Enter the index of the laptop: "))
    #laptop_name = input("Enter the name of the laptop: ")
    customer_name = input("Enter the name of the customer: ")
    quantity = int(input("Enter the quantity sold: "))
    # date = input("Enter the date of sale (YYYY-MM-DD): ")
    
    selected_laptop = inventory[laptop_index - 1]

    # Update the inventory
    # inventory[laptop_name]['quantity'] -= quantity
    update_laptop_inventory(
        'inventory.txt', selected_laptop['name'], quantity, type='sell')

    # Generate the sale invoice
    invoice = generate_sale_invoice(
        customer_name, selected_laptop['name'], selected_laptop['price'], quantity, 50)
    write_sell_invoice_to_file(invoice)
