class Product:
    """Класс для представления продуктов."""

    def __init__(
            self, name, description,
            price, quantity_in_stock,
    ):
        self.name: str = name
        self.description: str = description
        self.price: float = round(price, 2)
        self.quantity_in_stock: int = quantity_in_stock

    @classmethod
    def create_or_update_product(
            cls, name, description, price,
            quantity_in_stock, products_list: list):
        """
        Создаёт товар или обновляет существующий в списке `products_list`
        В случае, если товар с таким именем есть в списке,
        обновляет его количество и выбирает наибольшую цену.
        """
        for product in products_list:
            if product.name == name:
                product.quantity_in_stock += quantity_in_stock
                product.price = max(product.price, round(price, 2))
                return product
        new_product = cls(name, description, price, quantity_in_stock)
        products_list.append(new_product)
        return new_product
