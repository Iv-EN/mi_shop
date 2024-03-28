from .product import Product


class Category:
    """Класс для представления категорий."""
    name: str
    description: str
    goods: list[Product]
    count_categories = 0
    count_unique_products = 0
    unique_products = set()

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_categories += 1
        Category.unique_products.update(set(self.goods))
        Category.count_unique_products = len(Category.unique_products)
