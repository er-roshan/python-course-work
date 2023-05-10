from stock import list_laptops
from sell_laptop import sell_laptop
from order_laptop import order_laptop


def main():
    # Load the inventory from file
    #inventory = read_laptop_inventory('inventory.txt')

    while True:
        print('''Welcome to my laptop shop!''')

        # Prompt the user for the transaction type
        print("\nWhat type of transaction would you like to perform?")
        print("1. See Available Laptops")
        print("2. Sell a laptop")
        print("3. Buy a laptop")
        print("4. Quit")

        transaction_type = int(input("Enter your choice: "))

        # Process the chosen transaction
        if transaction_type == 1:
            list_laptops()
        elif transaction_type == 2:
            sell_laptop()
        elif transaction_type == 3:
            order_laptop()
        elif transaction_type == 4:
            # Quit the program
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
