from products import Product
from typing import List

class Store:
    def __init__(self, product_list):
        self.products = product_list[:]

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for prod in self.products:
            total += prod.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        active_products = []
        for prod in self.products:
            if prod.is_active():
                active_products.append(prod)
        return active_products

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, qty in shopping_list:
            total_price += product.buy(qty)
        return total_price