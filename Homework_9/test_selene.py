import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "engovadzip")
@allure.description("Test with allure steps")
@allure.feature("Search issue on GitHub")
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open("https://github.com")

    s("//button[@data-target='qbsearch-input.inputButton']").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#81")).should(be.visible)