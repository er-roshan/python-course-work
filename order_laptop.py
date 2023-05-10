from file_handling import read_laptop_inventory, update_laptop_inventory
from invoice import generate_order_invoice, write_buy_invoice_to_file

def order_laptop():
    inventory = read_laptop_inventory('inventory.txt')
    # Buy a laptop
    distributor_name = input("Enter the name of the distributor: ")
    laptop_name = input("Enter the name of the laptop: ")
    quantity = int(input("Enter the quantity to buy: "))
    for laptop in inventory:
        if laptop['name'] == laptop_name:
            brand_name = laptop['brand']
            net_amount = quantity * laptop['price']
            break
        else:
            print("Laptop is not available")
    # date = input("Enter the date of purchase (YYYY-MM-DD): ")
    shipping_cost = float(input("Enter the shipping cost: "))
    vat_amount = round(net_amount * 0.13, 2)
    gross_amount = net_amount + vat_amount + shipping_cost

    # Update the inventory
    update_laptop_inventory(
        'inventory.txt', laptop_name, quantity, type='buy')

    # Generate the order invoice
    invoice = generate_order_invoice(
        distributor_name, laptop_name, brand_name, quantity, net_amount, shipping_cost, vat_amount)
    write_buy_invoice_to_file(invoice)
