from .abstract_classes import BaseClass
from .exceptions import ZeroQuantityException
from .product import Product


class Order(BaseClass):
    def __init__(self, name: str, product: Product, quantity: int) -> None:
        super().__init__(name)
        try:
            if quantity == 0:
                raise ZeroQuantityException(
                    "Количество товара в заказе не может быть нулевым"
                )
        except ZeroQuantityException as e:
            print(e)
            raise ValueError()
        else:
            self.product = product
            self.quantity = quantity
            print("Товар успешно добавлен в заказ")
        finally:
            print("Обработка добавления товара в заказ завершена")

    @property
    def total_cost(self):
        return self.product.__price * self.quantity

    def __str__(self) -> str:
        return (
            f"Заказ: {self.name}, продукт: {self.product.name}, "
            f"количество: {self.quantity}"
        )
