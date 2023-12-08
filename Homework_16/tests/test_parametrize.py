import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (360, 740)])
def browser_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("browser_setup", [(1920, 1080)], ids=['1280 * 960'], indirect=True)
def test_github_desktop(browser_setup):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_setup", [(360, 740)], ids=['360 * 640'], indirect=True)
def test_github_mobile(browser_setup):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))