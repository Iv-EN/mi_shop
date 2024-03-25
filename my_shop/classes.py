class Product:
    """Класс для представления продуктов."""
    def __init__(
            self, name, description,
            price, quantity_in_stock,
    ):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock



class Category:
    """Класс для представления категорий."""
    categories_count = 0
    unique_goods = set()
    unique_count = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.categories_count += 1
        for product in goods:
            Category.unique_goods.add(product.name)
        Category.unique_count = len(Category.unique_goods)
