import json
import tempfile
from pathlib import Path

import pytest

from my_shop.category import Category
from my_shop.utils import load_data_from_json


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
                "Современный телевизор, который позволяет наслаждаться "
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
        "Современный телевизор, который позволяет наслаждаться "
        "просмотром, станет вашим другом и помощником"
    )
    assert len(categories[1].goods) == 1
    assert categories[1].goods[0].name == "55\" QLED 4K"
    assert categories[1].goods[0].price == 123000.0
    assert categories[1].goods[0].description == "Фоновая подсветка"
    assert categories[1].goods[0].quantity_in_stock == 7
    Path(json_file).unlink()
