import csv

def create_and_stock_shop():
    shop = {}
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        shop["cash"] = float(first_row[0])
        shop["products"] = []
        for row in csv_reader:
            product = {}
            product["name"] = row[0]
            product["price"] = float(row[1])
            product["quantity"] = int(row[2])
            shop["products"].append(product)
    return shop


def read_customer(file_path):
    customer = {}
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        customer["name"] = first_row[0]
        customer["cash"] = float(first_row[1])
        customer["products"] = []
        for row in csv_reader:
            product = {}
            product["name"] = row[0]
            product["quantity"] = int(row[1])
            customer["products"].append(product)
    return customer


def process_order(shop, customer):
    total_order_cost = 0
    
    for product in customer["products"]:
        for shop_product in shop["products"]:
            if product["name"] == shop_product["name"]:
                order_cost = product["quantity"] * shop_product["price"]
                
                if product["quantity"] <= shop_product["quantity"] and customer["cash"] >= order_cost:
                    shop["cash"] += order_cost
                    shop_product["quantity"] -= product["quantity"]
                    total_order_cost += order_cost
                    print(f"Order processed for {product['name']} quantity: {product['quantity']}")
                elif product["quantity"] > shop_product["quantity"]:
                    print(f"Not enough stock for {product['name']}")
                else:
                    print(f"Not enough money for {product['name']}")
                break
    
    if total_order_cost > 0:
        print(f"Total order cost: {total_order_cost}")
        print(f"Remaining cash in the shop: {shop['cash']}")
    else:
        print("No valid orders processed.")




def print_product(product):
    print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')


def print_customer(customer):
    print(f'NAME: {customer["name"]}, CASH: {customer["cash"]}')
    for product in customer["products"]:
        print(f'NAME: {product["name"]}, QUANTITY: {product["quantity"]}')


def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    for product in shop["products"]:
        print_product(product)


# First customer
shop = create_and_stock_shop()
print_shop(shop)

customer = read_customer('customer.csv')
print_customer(customer)
process_order(shop, customer)

# Second customer
customer1 = read_customer('customertest.csv')
print_customer(customer1)
process_order(shop, customer1)

# Third customer
customer2 = read_customer('customertest2.csv')
print_customer(customer2)
process_order(shop, customer2)
