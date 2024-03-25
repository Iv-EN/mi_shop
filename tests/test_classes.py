from my_shop.classes import Category, Product


def test_category():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    product2 = Product("Рубашка", "Офисная", 1500, 50)
    product3 = Product("Кроссовки", "Спортивные", 5000, 100)
    product4 = Product("Ботинки", "Повседневные", 7500, 2)
    category1 = Category("Обувь", "Все для ног", [product1, product3])
    category2 = Category("Одежда", "Все для тела", [product2, product4])
    assert  category1.name == "Обувь"
    assert  category1.description == "Все для ног"
    assert  category1.goods == [product1, product3]
    assert category2.goods == [product2, product4]
    assert Category.categories_count == 2
    assert Category.unique_count == 3

def test_product():
    product1 = Product("Кроссовки", "Спортивные", 5000, 100)
    assert product1.name == "Кроссовки"
    assert product1.description == "Спортивные"
    assert  product1.price == 5000
    assert  product1.quantity_in_stock == 100