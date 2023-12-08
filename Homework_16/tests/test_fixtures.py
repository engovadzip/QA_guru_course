import pytest
from selene import browser, have


@pytest.fixture
def desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def mobile():
    browser.config.window_width = 360
    browser.config.window_height = 740


def test_github_desktop(desktop):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))