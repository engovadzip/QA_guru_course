from selene import browser
from selene import be, have

def test_lesson2():
    browser.open('https://google.com')
    browser.element('textarea[name="q"]').type('дпруклыплкуыптлдыкутылдьмымвмыудкпьдуыки').press_enter()
    browser.element('#botstuff').should(have.text('не найдено'))

def test_lesson1():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))