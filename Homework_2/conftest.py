from selene.support.shared import browser
import pytest

@pytest.fixture(scope="session", autouse=True)
def whole_window():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()