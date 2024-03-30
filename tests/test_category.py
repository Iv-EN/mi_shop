from my_shop.category import Category
from my_shop.product import Product


def test_category():
    product1 = Product("Кроссовки", "Спортивные", 5000.553, 100)
    product2 = Product("Рубашка", "Офисная", 1500, 50)
    product3 = Product("Кроссовки", "Спортивные", 5000.553, 100)
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
    assert Category.count_categories == 2
    assert Category.count_unique_products == 4

    actual_goods = category1.get_goods
    expected_goods = [
        "Кроссовки, 5000.55 руб. Остаток: 100 шт.",
        "Рубашка, 1500 руб. Остаток: 50 шт."
    ]
    assert actual_goods == expected_goods
