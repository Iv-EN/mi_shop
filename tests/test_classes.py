import json
import tempfile
from pathlib import Path

import pytest

from my_shop.classes import Category, Product
from my_shop.utilities import load_data_from_json


@pytest.fixture
def json_file():
    data = [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации, но"
                "и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": (
                "Современный телевизор, который позволяет наслаждаться"
                "просмотром, станет вашим другом и помощником"
            ),
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp_file:
        json.dump(data, tmp_file)
    return tmp_file.name


def test_category():
    product1 = Product("Кроссовки", "Спортивные", 5000.553, 100)
    product2 = Product("Рубашка", "Офисная", 1500, 50)
    product3 = Product("Кроссовки", "Спортивные", 5000, 100)
    product4 = Product("Ботинки", "Повседневные", 7500, 2)
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
    assert Category.categories_count == 2
    assert Category.get_unique_names_count() == 3


def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert product1.price == 5000
    assert product1.quantity_in_stock == 100


def test_load_data_from_json(json_file):
    categories = load_data_from_json(json_file)
    assert len(categories) == 2
    assert all(isinstance(category, Category) for category in categories)
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == (
        "Смартфоны, как средство не только коммуникации, но"
        "и получение дополнительных функций для удобства жизни"
    )
    assert len(categories[0].goods) == 3
    assert categories[0].goods[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].goods[0].description == (
        "256GB, Серый цвет, 200MP камера")
    assert categories[0].goods[0].price == 180000.0

    assert categories[1].name == "Телевизоры"
    assert categories[1].description == (
        "Современный телевизор, который позволяет наслаждаться"
        "просмотром, станет вашим другом и помощником"
    )
    assert len(categories[1].goods) == 1
    assert categories[1].goods[0].name == "55\" QLED 4K"
    assert categories[1].goods[0].price == 123000.0
    assert categories[1].goods[0].description == "Фоновая подсветка"
    assert categories[1].goods[0].quantity_in_stock == 7
    Path(json_file).unlink()
