from .abstract_classes import BaseClass, BaseProduct
from .mixins import MixinObjectCreationInfo


class Product(BaseClass, MixinObjectCreationInfo, BaseProduct):
    """Класс для представления продуктов."""

    def __init__(self, name, description, price, quantity_in_stock, color):
        super().__init__(name)
        self.description: str = description
        self.__price: float = None
        self.price = price
        self.quantity_in_stock: int = quantity_in_stock
        self.color = color

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price} руб. Остаток: "
            f"{self.quantity_in_stock} шт."
        )

    def __add__(self, other):
        if type(self) is type(other):
            return (
                self.price * self.quantity_in_stock
                + other.price * other.quantity_in_stock
            )
        raise TypeError("Товары разных классов складывать нельзя")

    @classmethod
    def create_or_update_product(cls, product_data: dict, products_list: list):
        """Создаёт товар или обновляет существующий в списке `products_list`

        В случае, если товар с таким именем есть в списке,
        обновляет его количество и выбирает наибольшую цену.
        """
        name = product_data["name"]
        for product in products_list:
            if product.name == name:
                product.quantity_in_stock += product_data["quantity_in_stock"]
                product.price = max(
                    product.price, round(product_data["price"], 2)
                )
                return product
        new_product = cls(**product_data)
        products_list.append(new_product)
        return new_product

    @property
    def price(self):
        """Геттер для цены проодукта."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены продукта."""
        if value < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = round(value, 2)


class Smartphone(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity_in_stock,
        color,
        performance,
        model,
        build_memory_capacity,
    ):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.performance = performance
        self.model = model
        self.build_memory_capacity = build_memory_capacity


class LawnGrass(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity_in_stock,
        color,
        manufacturer_country,
        germination_period,
    ):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
