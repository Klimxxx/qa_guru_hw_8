"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        equal_quantity = product.quantity
        assert product.check_quantity(equal_quantity)

        less_quantity = product.quantity - 1
        assert product.check_quantity(less_quantity)

        more_quantity = product.quantity + 1
        assert not product.check_quantity(more_quantity)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity ==1

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        more_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(more_quantity) == ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, pencil, cart):
        cart.add_product(pencil, quantity=5)
        assert cart.products(pencil) == 5

        cart.add_product(pencil, quantity=100)
        assert cart.products(pencil) == 105

    def test_remove_product(self, product:Product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 1)
        cart.remove_product(product, 5000)
        assert product not in cart.products

    def test_clear(self, cart, copybook, product, pencil):
        cart.add_product(copybook, 150)
        cart.add_product(pencil, 500)
        cart.clear()

        assert cart.products == {}


    def test_get_total_price(self, cart, pencil, copybook):
        cart.add_product(pencil, 4)
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)

        assert cart.get_total_price() == 300


    def test_buy(self, cart, pencil, copybook, product):
        cart.add_product(pencil, 4)
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.buy()

        assert pencil.quantity == 996
        assert product.quantity == 999
        assert copybook.quantity == 2998


    def test_buy_more_than_stock(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()









