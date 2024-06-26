import pytest

from my_shop.category import Category
from my_shop.product import Product


@pytest.fixture
def sample_product():
    return Product("Тестовый продукт", "Описание", 100, 10, "Чёрный")


@pytest.fixture
def another_product():
    return Product("Другой продукт", "Описание", 150, 5, "Белый")


@pytest.fixture
def category_one():
    return Category(
        "Тестовая категория",
        "Все чистого кода",
        [sample_product, another_product],
    )


def test_category():
    product1 = Product("Кроссовки", "Спортивные", 5000.553, 100, "Белый")
    product2 = Product("Рубашка", "Офисная", 1500, 50, "В клеточку")
    product3 = Product(
        "Кроссовки", "Спортивные", 5000.553, 100, "Белые с красным"
    )
    product4 = Product("Ботинки", "Повседневные", 7500, 2, "Коричневые")
    category1 = Category("Обувь", "Все для ног", [product1, product2])
    category2 = Category("Одежда", "Все для тела", [product3, product4])
    assert category1.name == "Обувь"
    assert category1.description == "Все для ног"
    assert category1.goods[0].name == "Кроссовки"
    assert category1.goods[0].description == "Спортивные"
    assert category1.goods[0].price == 5000.55
    assert category1.goods[0].quantity_in_stock == 100
    assert category1.goods[1].name == "Рубашка"
    assert category1.goods[1].description == "Офисная"
    assert category1.goods[1].price == 1500
    assert category1.goods[1].quantity_in_stock == 50
    assert category2.name == "Одежда"
    assert category2.description == "Все для тела"
    assert Category.count_categories == 2
    assert Category.count_unique_products == 4

    actual_goods = category1.get_goods
    expected_goods = [
        "Кроссовки, 5000.55 руб. Остаток: 100 шт.",
        "Рубашка, 1500 руб. Остаток: 50 шт.",
    ]
    assert actual_goods == expected_goods
    assert len(category1) == 150
    assert str(category2) == "Одежда, количество продуктов: 102 шт."
    assert (
        repr(category1) == "Category(name='Обувь', description='Все для ног',"
        " _Category__goods=[Product(name='Кроссовки'"
        ", description='Спортивные', _Product__price=5000.55,"
        " quantity_in_stock=100, color='Белый'),"
        " Product(name='Рубашка', description='Офисная', _Product__price=1500,"
        " quantity_in_stock=50, color='В клеточку')])"
    )
    assert category1.get_average_price() == 3250.28
    no_products = Category("Одежда", "Все для тела", [])
    assert no_products.get_average_price() == 0


# def test_get_average_price(category_one: Category):
#    average_price = category_one.get_average_price()
#    assert average_price == 125
