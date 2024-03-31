from my_shop.product import Product


def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert product1.price == 5000
    assert product1.quantity_in_stock == 100

    product_list = []
    product_data1 = {
        "name": "Батон",
        "description": "Нарезной",
        "price": 52,
        "quantity_in_stock": 100
    }
    product_data2 = {
        "name": "Батон",
        "description": "Молочный",
        "price": 54.25,
        "quantity_in_stock": 75
    }
    product2 = Product.create_or_update_product(product_data1, product_list)
    assert product2.name == "Батон"
    assert product2.price == 52
    assert product2.description == "Нарезной"
    assert product2.quantity_in_stock == 100
    product3 = Product.create_or_update_product(product_data2, product_list)  # noqa
    assert product2.price == 54.25
    assert product2.quantity_in_stock == 175


def test_product_price_negative(capsys):
    product_list = []
    product_data3 = {
        "name": "тест",
        "description": "проверка отрицательной цены",
        "price": -54.25,
        "quantity_in_stock": 75
    }
    Product.create_or_update_product(product_data3, product_list)
    captured = capsys.readouterr()
    assert "Цена не может быть отрицательной" in captured.out
