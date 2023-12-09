import csv

def create_and_stock_shop():
    shop = []
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first_row = next(csv_reader)
        shop["cash"] = float(first_row)
        shop["products"] = []
        for row in csv_reader:
            product ={}

            product["name"] = row[0]
            product["price"] = row[1]
            product["quantity"] = row[2]

            shop["products"].append(product)
