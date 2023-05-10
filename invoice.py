import os
from datetime import date
import datetime

def generate_sale_invoice(customer_name, laptop_name, laptop_price, quantity, shipping_cost):
    """
    Generates an invoice for a laptop sale.
    """
    today = date.today()
    invoice_number = 'S{:04d}'.format(today.toordinal())
    subtotal = laptop_price * quantity
    total = subtotal + shipping_cost
    invoice = {
        'invoice_number': invoice_number,
        'date': str(today),
        'customer_name': customer_name,
        'laptop_name': laptop_name,
        'price': laptop_price,
        'quantity': quantity,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total': total
    }
    return invoice


def generate_order_invoice(distributor_name, laptop_name, brand_name, quantity, net_amount, shipping_cost, vat_amount):
    """
    Generates an invoice for a laptop order.
    """
    today = date.today()
    invoice_number = 'O{:04d}'.format(today.toordinal())
    subtotal = net_amount + vat_amount
    total = subtotal + shipping_cost
    invoice = {
        'invoice_number': invoice_number,
        'date': str(today),
        'distributor_name': distributor_name,
        'laptop_name': laptop_name,
        'brand_name': brand_name,
        'quantity': quantity,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'vat_amount': vat_amount,
        'total': total
    }
    return invoice


def write_sell_invoice_to_file(invoice):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory = 'invoice/sell'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = '{}/sell_invoice_{}.txt'.format(directory, timestamp)
    with open(filename, 'w') as file:
        file.write('Invoice Number: {}\n'.format(invoice['invoice_number']))
        file.write('Date: {}\n'.format(invoice['date']))
        file.write('Customer Name: {}\n'.format(invoice['customer_name']))
        file.write('Laptop Name: {}\n'.format(invoice['laptop_name']))
        file.write('Price: ${:.2f}\n'.format(invoice['price']))
        file.write('Quantity: {}\n'.format(invoice['quantity']))
        file.write('Subtotal: ${:.2f}\n'.format(invoice['subtotal']))
        file.write('Shipping Cost: ${:.2f}\n'.format(invoice['shipping_cost']))
        file.write('Total: ${:.2f}\n'.format(invoice['total']))
        file.write('\n')
    print("Item sold and Invoice Generated")


def write_buy_invoice_to_file(invoice):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory = 'invoice/buy'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = '{}/buy_invoice_{}.txt'.format(directory, timestamp)
    with open(filename, 'w') as file:
        file.write('Invoice Number: {}\n'.format(invoice['invoice_number']))
        file.write('Date: {}\n'.format(invoice['date']))
        file.write('Distributor Name: {}\n'.format(invoice['distributor_name']))
        file.write('Laptop Name: {}\n'.format(invoice['laptop_name']))
        file.write('Brand Name: {}\n'.format(invoice['brand_name']))
        file.write('Quantity: {}\n'.format(invoice['quantity']))
        file.write('Net Amount: ${:.2f}\n'.format(invoice['subtotal']))
        file.write('VAT Amount: ${:.2f}\n'.format(invoice['vat_amount']))
        file.write('Shipping Cost: ${:.2f}\n'.format(invoice['shipping_cost']))
        file.write('Total: ${:.2f}\n'.format(invoice['total']))
        file.write('\n')
    print("Item ordered and Invoice Generated")
