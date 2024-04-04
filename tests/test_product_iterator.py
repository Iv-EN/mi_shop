import pytest

from my_shop.category import Category
from my_shop.product import Product
from my_shop.product_iterator import ProductIterator


def test_product_iterator():
    product1 = Product("Кроссовки", "Спортивные", 5000.553, 100)
    product2 = Product("Ботинки", "Повседневные", 7500, 2)
    goods = [product1, product2]
    category1 = Category("Обувь", "Все для ног", goods)
    category2 = Category("Обувь", "Все для ног", [])
    iterator = ProductIterator(category1)
    for good in goods:
        assert next(iterator) == good
    category2 = Category("Обувь", "Все для ног", [])
    iterator2 = ProductIterator(category2)
    with pytest.raises(StopIteration):
        next(iterator2)
