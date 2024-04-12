from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс (шаблон) для создания продуктов."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __add__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def create_or_update_product(cls, product_data: dict, products_list: list):
        """Создаёт товар или обновляет существующий в списке `products_list`

        В случае, если товар с таким именем есть в списке,
        обновляет его количество и выбирает наибольшую цену.
        """

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены проодукта."""

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены продукта."""


class BaseClass(ABC):
    """Aбстрактный класс шаблон с общим свойством `name`."""

    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        pass
