import os
import csv
import random
import string


def get_header():
    with open('catalog_products.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)

    # Fixes handleId otherwise starting with strange characters in front for some reason
    header[0] = "handleId"

    headerDict = {}
    for key in header:
        headerDict[key] = ''

    return headerDict

def clear_CSV():
    header = get_header()
    for key in header:
        header[key] = key
    with open('catalog_products.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header.keys())
        writer.writerow(header)

def create_CSV():
    for i, item in enumerate(ITEMS):
        row = get_header()
        row['fieldType'] = 'Product'
        row['name'] = f"Mystery {LINES[i]} {ITEMS[i]}"
        itemlist = item.split(" ")
        itemlist.insert(0, LINES[i])
        collection = ";".join(itemlist)

        row['collection'] = collection
        row['price'] = PRICES[i]
        row['visible'] = 'TRUE'
        row['discountMode'] = 'PERCENT'
        row['discountValue'] = '0'
        row['inventory'] = 'InStock'
        row['additionalInfoTitle1'] = 'Buy Link (Click me)'
        row['additionalInfoDescription1'] = f'<p><a href="{BUY_LINKS[i]}" target="_blank">Buy</a></p>'
        row['handleId'] = get_random_string()
        row['productImageUrl'] = IMAGE_LINKS[i]
        with open('catalog_products.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writerow(row)

def get_choice():
    choice = input("What choice?"
                   "\n1 - Revival"
                   "\n2 - Everyday\n")
    match choice:
        case '1':
            return "Revival"
        case '2':
            return "Everyday"

# This is used to create a unique handleid. Duplicate handleids on wix result in the product simply getting overriden.
def get_random_string(): 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def get_column(filename, column):
    column_list = []

    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for col in reader:
            column_list.append(col[column])
    
    return column_list

def get_price(line, type):
    if (line == "Revival" and type == "T-Shirt"): return '30'
    elif (line == "Revival" and type == "Pants"): return '50'
    elif (line == "Revival" and type == "Sweater"): return '60'
    elif (line == "Revival" and type == "Jacket"): return '100'
    elif (line == "Everyday" and type == "T-Shirt"): return '20'
    elif (line == "Everyday" and type == "Pants"): return '35'
    elif (line == "Everyday" and type == "Sweater"): return '40'
    elif (line == "Everyday" and type == "Jacket"): return '60'





LINES = get_column('purchase_buttons.csv', 'Line')
ITEMS = get_column('purchase_buttons.csv', 'Item')
BUY_LINKS = get_column('purchase_buttons.csv', 'Link')
PRICES = get_column('purchase_buttons.csv', 'Price')
IMAGE_LINKS = get_column('purchase_buttons.csv', 'Image')

clear_CSV()
create_CSV()


