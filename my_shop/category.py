from .product import Product


class Category:
    """Класс для представления категорий."""
    count_categories = 0
    count_unique_products = 0
    unique_products = set()

    def __init__(self, name, description, goods=None):
        if goods is None:
            goods = []
        self.name: str = name
        self.description: str = description
        self.__goods: list[Product] = goods
        Category.count_categories += 1
        Category.unique_products.update(set(self.__goods))
        Category.count_unique_products = len(Category.unique_products)

    @property
    def add_product(self, product: Product):
        self.__goods.append(product)
        Category.unique_products.add(product)
        Category.count_unique_products = len(Category.unique_products)

    @property
    def goods(self):
        return self.__goods
