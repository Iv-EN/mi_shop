from my_shop.product import Product


def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    product4 = Product("Батон", "Нарезной", 52, 100)
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert product1.price == 5000
    assert product1.quantity_in_stock == 100

    product_list = []
    product2 = Product.create_or_update_product(
        "Батон", "Нарезной", 52, 100, product_list
    )
    assert product2.name == "Батон"
    assert product2.quantity_in_stock == 100
    product3 = Product.create_or_update_product(  # noqa
        "Батон", "Молочный", 54.25, 75, product_list
    )
    assert product2.price == 54.25
    assert product2.quantity_in_stock == 175
    assert str(product1) == "Кроссовки, 5000 руб. Остаток: 100 шт."
    assert product1 + product4 == 505200
