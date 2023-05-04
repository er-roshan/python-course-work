from file_handling import read_laptop_inventory, update_laptop_inventory
from validation import get_validated_input, validate_customer_name, validate_quantity, validate_shipping_cost, validate_date
from invoice import generate_sale_invoice, generate_order_invoice, write_buy_invoice_to_file, write_sell_invoice_to_file

def main():
    # Load the inventory from file
    inventory = read_laptop_inventory('inventory.txt')

    while True:
        # Display the available laptops
        print("\nAvailable Laptops:")
        for laptop in inventory:
            print(laptop)

        # Prompt the user for the transaction type
        print("\nWhat type of transaction would you like to perform?")
        print("1. Sell a laptop")
        print("2. Buy a laptop")
        print("3. Quit")

        transaction_type = int(input("Enter your choice: "))

        # Process the chosen transaction
        if transaction_type == 1:
            # Sell a laptop
            laptop_name = input("Enter the name of the laptop: ")
            customer_name = input("Enter the name of the customer: ")
            quantity = int(input("Enter the quantity sold: "))
            date = input("Enter the date of sale (YYYY-MM-DD): ")

            # Update the inventory
            #inventory[laptop_name]['quantity'] -= quantity
            update_laptop_inventory('inventory.txt', laptop_name, quantity, type = 'sell')
            for laptop in inventory:
                if laptop['name'] == laptop_name:
                    price = laptop['price']
                    break
                else:
                    print("Laptop is not available")

            # Generate the sale invoice
            invoice = generate_sale_invoice(customer_name, laptop_name, price, quantity, 50)
            write_sell_invoice_to_file(invoice)

        elif transaction_type == 2:
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
            #date = input("Enter the date of purchase (YYYY-MM-DD): ")
            shipping_cost = float(input("Enter the shipping cost: "))
            vat_amount = round(net_amount * 0.13, 2)
            gross_amount = net_amount + vat_amount + shipping_cost

            # Update the inventory
            update_laptop_inventory('inventory.txt', laptop_name, quantity, type = 'buy')

            # Generate the order invoice
            invoice = generate_order_invoice(distributor_name, laptop_name, brand_name, quantity, net_amount, shipping_cost, vat_amount)
            write_buy_invoice_to_file(invoice)

        elif transaction_type == 3:
            # Quit the program
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
