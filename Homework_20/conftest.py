import pytest
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demowebshop.tricentis.com/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
