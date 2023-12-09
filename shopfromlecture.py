import csv

def create_and_stock_shop():
    shop = {}
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        shop ["cash"] = float(first_row[0])
        shop["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["price"] = row[1]
            product["quantity"] = row[2]

            shop["products"].append(product)

    return shop

    

def read_customer(file_path):
    pass
    


def print_product(product):
    print (f'NAME:{product["name"]}, PRICE:{product["price"]}, QUANTITY:{product["quantity"]}')
    
    

def print_customer(c):
    pass
    

def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    for product in shop["products"]:
     print_product(product)
    

shop = create_and_stock_shop()
print_shop(shop)

