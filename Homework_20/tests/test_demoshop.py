from selene import browser, command, have, query
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
            url=URL + "login",
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


def test_add_gift_card_to_cart_through_API():
    with allure.step('Open gift card description page'):
        browser.open(URL)
        browser.element('.product-title').should(have.text("Gift Card")).perform(command.js.scroll_into_view).click()
        browser.element("//h1").should(have.text("Gift Card"))
        product_name = browser.element('//h1').get(query.text)

    with allure.step('Add gift card to cart through API'):
        response = requests.post(
            url=URL + "/addproducttocart/details/2/1",
            data={
                "giftcard_2.RecipientName": "You",
                "giftcard_2.RecipientEmail": "your@email.com",
                "giftcard_2.SenderName": "Exam Ple",
                "giftcard_2.SenderEmail": "example1200@example.com",
                "giftcard_2.Message": "Happy New Year!",
                "addtocart_2.EnteredQuantity": 1
                }
        )

        assert response.status_code == 200

        with allure.step('Get cookie from API'):
            cookie = response.cookies.get("Nop.customer")

        with allure.step('Set cookie from API'):
            browser.open(URL)
            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
            browser.open(URL)

        with allure.step('Check that added product is in cart'):
            browser.element('.header-links .ico-cart').click()
            browser.element('.product-name').should(have.text(product_name))
            browser.element('.cart-item-row .attributes').should(have.text("You"))
            browser.element('.cart-item-row .attributes').should(have.text("your@email.com"))
            browser.element('.cart-item-row .attributes').should(have.text("Exam Ple"))
            browser.element('.cart-item-row .attributes').should(have.text("example1200@example.com"))
            browser.element('.qty-input').should(have.attribute('value', '1'))


def test_add_5_laptops_to_cart_through_API():
    with allure.step('Open "Notebooks" category'):
        browser.open(URL)
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

        with allure.step('Check that added product is in cart'):
            browser.element('.header-links .ico-cart').click()
            browser.element('.product-name').should(have.text(product_name))
            browser.element('.qty-input').should(have.attribute('value', '5'))
