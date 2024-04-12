from .abstract_classes import BaseClass
from .product import Product


class Order(BaseClass):
    def __init__(self, name, product: Product, quantity: int) -> None:
        super().__init__(name)
        self.product = product
        self.quantity = quantity
        self.total_cost = None

    @property
    def total_cost(self):
        return self.product.__price * self.quantity
