class Product:
    """Класс для представления продуктов."""

    def __init__(
            self, name, description,
            price, quantity_in_stock,
    ):
        self.name: str = name
        self.description: str = description
        self.__price: float = None
        self.price = price
        self.quantity_in_stock: int = quantity_in_stock

    @classmethod
    def create_or_update_product(
            cls, product_data: dict, products_list: list):
        """
        Создаёт товар или обновляет существующий в списке `products_list`
        В случае, если товар с таким именем есть в списке,
        обновляет его количество и выбирает наибольшую цену.
        """
        name = product_data['name']
        for product in products_list:
            if product.name == name:
                product.quantity_in_stock += product_data['quantity_in_stock']
                product.price = max(
                    product.price, round(product_data['price'], 2))
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
            raise ValueError("Цена не может быть отрицательной")
        self.__price = round(value, 2)
