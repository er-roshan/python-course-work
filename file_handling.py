def read_laptop_inventory(file_path):
    """
    Reads the laptop inventory from the given file and returns it as a list of dictionaries.
    Each dictionary corresponds to a laptop and contains its name, brand, price, quantity, processor details,
    and graphics card details.
    """
    laptops = []
    with open(file_path, 'r') as f:
        for line in f:
            # Split each line into its components and create a dictionary for the laptop
            components = line.strip().split(',')
            laptop = {
                'name': components[0],
                'brand': components[1],
                'price': float(components[2].replace('$', '')),
                'quantity': int(components[3]),
                'processor': components[4],
                'graphics_card': components[5]
            }
            laptops.append(laptop)
    return laptops


def write_laptop_inventory(file_path, laptops):
    """
    Writes the given list of laptops to the given file in the appropriate format.
    """
    with open(file_path, 'w') as f:
        for laptop in laptops:
            # Convert each laptop dictionary to a formatted string and write it to the file
            line = '{},{},${},{},{},{}\n'.format(laptop['name'], laptop['brand'], laptop['price'],
                                                 laptop['quantity'], laptop['processor'], laptop['graphics_card'])
            f.write(line)


def update_laptop_inventory(file_path, laptop_name, quantity_change, type):
    """
    Updates the quantity of the laptop with the given name in the inventory file by the given amount.
    """
    laptops = read_laptop_inventory(file_path)
    updated = False
    for laptop in laptops:
        if laptop['name'] == laptop_name:
            if(type == 'sell'):
                laptop['quantity'] -= quantity_change
            else:
                laptop['quantity'] += quantity_change
            updated = True
            break
    if updated:
        write_laptop_inventory(file_path, laptops)
        print(f"Inventory for {laptop_name} updated.")
    else:
        print(f"Laptop {laptop_name} not found in inventory.")
