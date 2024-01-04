from selene import browser, have, query
import allure
import requests
import time


URL = 'https://demowebshop.tricentis.com/'
LOGIN = "example1200@example.com"
PASSWORD = "123456"


def test_log_in_demoshop_through_API():
    with allure.step('Open "Log in" page'):
        browser.open('')
        browser.element('.ico-login').click()
        browser.element('.email')

    with allure.step('Login through API'):
        response = requests.post(
            url=URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )

    with allure.step('Get cookie from API'):
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step('Set cookie from API'):
        browser.open(URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(URL)

    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.text(LOGIN))


@allure.step('Clearing cart if necessary')
def test_clear_cart():
    cart = browser.element('.header-links .ico-cart').get(query.text)

    if '(0)' in cart:
        pass

    else:
        with allure.step('Open cart'):
            browser.element('.header-links .ico-cart').click()

        with allure.step('Remove products from cart'):
            checks = browser.all('[name="removefromcart"]')
            for el in checks:
                el.click()

            browser.element('[name="updatecart"]').click()

        with allure.step('Check that cart is empty'):
            browser.element('.order-summary-content').should(have.text('Cart is empty'))

def test_add_laptop_to_cart_through_API():
    with allure.step('Open "Notebooks" category'):
        browser.element('.top-menu a[href="/computers"]').hover()
        browser.element('.top-menu a[href="/notebooks"]').click()
        browser.element("//h1").should(have.text("Notebooks"))

    with allure.step('Open laptop description page'):
        product_name = browser.element('.product-title').get(query.text)

        browser.element('.product-title').click()
        browser.element('.product-name').should(have.text(product_name))

    with allure.step('Add laptop to cart through API'):
        response = requests.post(
            url=URL + "addproducttocart/details/31/1",
            data={"addtocart_31.EnteredQuantity": 5}
        )

        assert response.status_code == 200

        with allure.step('Get cookie from API'):
            cookie = response.cookies.get("Nop.customer")

        with allure.step('Set cookie from API'):
            browser.open(URL)
            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
            browser.open(URL)

        with allure.step('Check that added product in cart'):
            browser.element('.header-links .ico-cart').click()
            browser.element('.product-name').should(have.text(product_name))