import json
import os

from .category import Category
from .product import Product

MAIN_PATH = os.path.dirname(__file__)
OPERATIONS_PATH = os.path.join(MAIN_PATH, 'data', 'products.json')


def load_data_from_json(filename):
    """Загружает данные категорий и товаров из файла JSON."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        products_in_category = []
        for product_data in category_data['products']:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity_in_stock=product_data['quantity']
            )
            products_in_category.append(product)
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            goods=products_in_category
        )
        categories.append(category)
    return categories
