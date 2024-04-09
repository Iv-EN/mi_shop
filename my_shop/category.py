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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        number_of_products: int = 0
        for good in self.__goods:
            number_of_products += good.quantity_in_stock
        return number_of_products

    def add_product(self, product: Product):
        """
        Добавляет продукт в список товаров категории
        и обновляет уникальные продукты.
        """
        if not isinstance(product, Product):
            print("Добавляемый объект должен быть наследником класса Product")
            return
        if product not in self.__goods:
            self.goods.append(product)
            Category.unique_products.add(product)
            Category.count_unique_products = len(Category.unique_products)

    @property
    def goods(self):
        """Возвращает список товаров категории."""
        return self.__goods

    @property
    def get_goods(self):
        """Возвращает строковую информацию о товаров в категории."""
        return [str(product) for product in self.__goods]
