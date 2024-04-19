import pytest

from my_shop.order import Order

from .test_product import sample_product  # noqa


def test_successful_order_creation(
    sample_product, capsys: pytest.CaptureFixture[str]  # noqa
):
    """Проверка успешного создания заказа."""
    test_order = Order("Тестовый заказ", sample_product, 2)  # noqa
    captured = capsys.readouterr()
    assert (
        "Товар успешно добавлен в заказ\n"
        "Обработка добавления товара в заказ завершена\n" in captured.out
    )


def test_otrying_add_product_zero_quantity(
    sample_product, capsys: pytest.CaptureFixture[str]  # noqa
):
    """Проверка попытки создать заказ с нулевым количеством продукта."""
    with pytest.raises(ValueError):
        test_order = Order("Тестовый заказ", sample_product, 0)  # noga
    captured = capsys.readouterr()
    assert "Количество товара в заказе не может быть нулевым\n"
    "Обработка добавления товара в заказ завершена\n" in captured.out
