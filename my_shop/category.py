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

    def add_product(self, product: Product):
        """
        Добавляет продукт в список товаров категории
        и обновляет уникалльные продукты.
        """
        if product not in self.__goods:
            self.__goods.append(product)
            Category.unique_products.add(product)
            Category.count_unique_products = len(Category.unique_products)

    @property
    def goods(self):
        """Возвращает список товаров категории."""
        return self.__goods

    def get_goods(self):
        """Возвращает строковую информацию о товаров в категории."""
        goods_list = []
        for good in self.__goods:
            goods_list.append(
                f'{good.name},'
                f' {good.price} руб. Остаток: {good.quantity_in_stock} шт.'
            )
        return goods_list
