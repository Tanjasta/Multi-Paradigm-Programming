from dataclasses import dataclass, field
from typing import List
import csv

@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass
class ProductStock:
    product: Product
    quantity: int

@dataclass
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

    def create_and_stock_shop(self, file_path):
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)

    def print_shop(self):
        print(f'Shop has {self.cash} in cash')
        for item in self.stock:
            print_product(item.product)
            print(f'The Shop has {item.quantity} of the above')

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

    @classmethod
    def read_customer(cls, file_path):
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            c = cls(first_row[0], float(first_row[1]))
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                c.shopping_list.append(ps)
            return c

    def print_customer(self):
        print(f'CUSTOMER NAME: {self.name} \nCUSTOMER BUDGET: {self.budget}')

        for item in self.shopping_list:
            print_product(item.product)
            print(f'{self.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
            cost = item.quantity * item.product.price
            print(f'The cost to {self.name} will be €{cost}')

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

# Usage
shop = Shop()
shop.create_and_stock_shop('stock.csv')
shop.print_shop()

customer = Customer.read_customer('customer.csv')
customer.print_customer()
