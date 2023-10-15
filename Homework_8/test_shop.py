import pytest

from .models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        product.buy(100)
        assert product.check_quantity(900)

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(9999)


class TestCart:
    def test_add_to_cart(self, product, cart):
        cart.add_product(product)
        assert product in cart.products
        assert cart.products.get(product) == 1
        
        cart.add_product(product)
        assert cart.products.get(product) == 2
    
    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 4)
        assert cart.products[product] == 6

    def test_clear(self, cart, product):
        cart.add_product(product, 19)
        cart.clear()
        assert not cart.products

    def test_total_price(self, cart, product):
        cart.add_product(product, 50)
        assert cart.get_total_price() == 5000

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_incorrect_quantity(self, cart, product):
        cart.add_product(product, 99999)
        with pytest.raises(ValueError):
            cart.buy()