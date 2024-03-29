from my_shop.product import Product


def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert product1.price == 5000
    assert product1.quantity_in_stock == 100
