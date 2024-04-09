import pytest

from my_shop.category import Category
from my_shop.product import Product
from my_shop.product_iterator import ProductIterator


def test_product_iterator():
    product1 = Product(
        "Кроссовки", "Спортивные", 5000.553, 100, "В ассортименте"
    )
    product2 = Product("Ботинки", "Повседневные", 7500, 2, "В ассортименте")
    goods = [product1, product2]
    category1 = Category("Обувь", "Все для ног", goods)
    iterator = ProductIterator(category1)
    for good in goods:
        assert next(iterator) == good
    with pytest.raises(StopIteration):
        next(iterator)
    category2 = Category("Обувь", "Все для ног", [])
    iterator2 = ProductIterator(category2)
    with pytest.raises(StopIteration):
        next(iterator2)
    category3 = Category("Обувь", "Все для ног", [product1])
    iterator3 = ProductIterator(category3)
    assert next(iterator3) == product1
    with pytest.raises(StopIteration):
        next(iterator3)
