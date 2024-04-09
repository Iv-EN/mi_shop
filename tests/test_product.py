import pytest

from my_shop.category import Category
from my_shop.product import Product, LawnGrass


@pytest.fixture
def sample_product():
    return Product("Тестовый продукт", "Описание", 100, 10, "Чёрный")


@pytest.fixture
def another_product():
    return Product("Другой продукт", "Описание", 150, 5, "Белый")


@pytest.fixture
def non_product():
    class NonProduct:
        def __init__(self) -> None:
            pass

    return NonProduct()


@pytest.fixture
def category():
    return Category("Электронника", "Электронные товары")


@pytest.fixture
def lawn_grass_product():
    return LawnGrass(
        "Трава", "Газонная", 1000, 8, "Зелёный", "Россия", "2 недели"
    )


def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100, "Белые")
    product4 = Product("Батон", "Нарезной", 52, 100, "Румяный")
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert product1.price == 5000
    assert product1.quantity_in_stock == 100

    product_list = []
    product_data1 = {
        "name": "Батон",
        "description": "Нарезной",
        "price": 52,
        "quantity_in_stock": 100,
        "color": "В ассортименте",
    }
    product_data2 = {
        "name": "Батон",
        "description": "Молочный",
        "price": 54.25,
        "quantity_in_stock": 75,
        "color": "В ассортименте",
    }
    product2 = Product.create_or_update_product(product_data1, product_list)
    assert product2.name == "Батон"
    assert product2.price == 52
    assert product2.description == "Нарезной"
    assert product2.quantity_in_stock == 100
    product3 = Product.create_or_update_product(  # noqa
        product_data2, product_list
    )
    assert product2.price == 54.25
    assert product2.quantity_in_stock == 175
    assert str(product1) == "Кроссовки, 5000 руб. Остаток: 100 шт."
    assert product1 + product4 == 505200


def test_product_price_negative(capsys):
    product_list = []
    product_data3 = {
        "name": "тест",
        "description": "проверка отрицательной цены",
        "price": -54.25,
        "quantity_in_stock": 75,
        "color": "в ассортименте",
    }
    Product.create_or_update_product(product_data3, product_list)
    captured = capsys.readouterr()
    assert "Цена не может быть отрицательной" in captured.out


def test_add_product_sucess(category: Category, sample_product: Product):
    """Проверка успешного добавления продукта в категорию."""
    initial_product_count = len(category.goods)
    category.add_product(sample_product)
    assert sample_product in category.goods
    assert len(category.goods) == initial_product_count + 1


def test_add_non_product(category, non_product):
    """Проверка попытки добавить объект не являющийся продуктом."""
    initial_product_count = len(category.goods)
    category.add_product(non_product)
    assert non_product not in category.goods
    assert len(category.goods) == initial_product_count


def test_add_method_sucess(sample_product, another_product):
    """Проверка успешной попытки сложить продукты (работа метода `__add__`)."""
    assert sample_product + another_product == 1750


def test_add_method_non_product(sample_product, non_product):
    """
    Проверка попытки сложить обекты разных классов (работа метода `__add__`).
    """
    with pytest.raises(TypeError):
        sample_product + non_product


def test_add_method_heir(sample_product, lawn_grass_product):
    """
    Проверка попытки сложить обекты наследники (работа метода `__add__`).
    """
    with pytest.raises(TypeError):
        sample_product + lawn_grass_product
