import re
from datetime import datetime

def validate_quantity(quantity):
    """
    Validates the quantity input by the user.
    """
    if not quantity.isnumeric():
        return False
    return True

def validate_price(price):
    """
    Validates the price input by the user.
    """
    if not re.match(r'^\d+(\.\d{1,2})?$', price):
        return False
    return True

def validate_name(name):
    """
    Validates the name input by the user.
    """
    if not name.isalpha():
        return False
    return True

def validate_email(email):
    """
    Validates the email input by the user.
    """
    if not re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?$', email):
        return False
    return True

def get_validated_input(prompt, validate_func):
    """
    Prompts the user with the given message and returns the user's input only if it passes the validation function.
    """
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_customer_name(name):
    """
    Returns True if the given name is not empty and contains only alphabetic characters and spaces.
    """
    if name.replace(' ', '').isalpha():
        return True
    else:
        return False

def validate_quantity(quantity):
    """
    Returns True if the given quantity is a positive integer.
    """
    try:
        quantity_int = int(quantity)
        if quantity_int > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_shipping_cost(cost):
    """
    Returns True if the given shipping cost is a positive float.
    """
    try:
        cost_float = float(cost)
        if cost_float > 0:
            return True
        else:
            return False
    except ValueError:
        return False



def validate_date(date_string):
    """
    Returns True if the given date string is in the format 'YYYY-MM-DD' and corresponds to a valid date.
    """
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        if date_obj.year < 1900:
            return False
        else:
            return True
    except ValueError:
        return False
