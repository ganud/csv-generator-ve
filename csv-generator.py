import csv


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
        # Isolate categories from the product names
        itemlist = item.split(" ")
        itemlist.insert(0, LINES[i])
        collection = ";".join(itemlist)
        row['collection'] = collection
        row['price'] = PRICES[i]
        row['visible'] = 'TRUE'
        row['discountMode'] = 'PERCENT'
        row['discountValue'] = '0'
        row['inventory'] = 'InStock'
        row['additionalInfoTitle1'] = 'Show Buy Link'
        row['additionalInfoDescription1'] = f'<p><a href="{BUY_LINKS[i]}" target="_blank">Add to Cart</a></p>'
        row['handleId'] = i + 20
        row['productImageUrl'] = IMAGE_LINKS[i]
        row['description'] = DESCRIPTIONS[i]
        row['productOptionName1'] = "Size Options (Specify in VE checkout)"
        row['productOptionType1'] = "DROP_DOWN"
        row['productOptionDescription1'] = "Small;Medium;Large"
        with open('catalog_products.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writerow(row)


def get_column(filename, column):
    column_list = []

    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for col in reader:
            column_list.append(col[column])
    
    return column_list


LINES = get_column('purchase_buttons.csv', 'Line')
ITEMS = get_column('purchase_buttons.csv', 'Item')
BUY_LINKS = get_column('purchase_buttons.csv', 'Link')
PRICES = get_column('purchase_buttons.csv', 'Price')
IMAGE_LINKS = get_column('purchase_buttons.csv', 'Image')
DESCRIPTIONS = get_column('purchase_buttons.csv', 'Description')

clear_CSV()
create_CSV()


