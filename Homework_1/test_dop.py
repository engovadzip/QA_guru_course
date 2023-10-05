from selene.support.shared import browser
from selene import be, have

browser.open('https://demoqa.com/text-box')
browser.element('#userName').click().type('my_name')
browser.element('#userEmail').click().type('mail@gmail.com')
browser.element('#currentAddress').click().type('Russia')
browser.element('#permanentAddress').click().type('Moscow')

browser.element('#submit').click()

browser.element('#output').should(be.visible)
browser.element('#output #name').should(have.text('my_name'))
browser.element('#output #email').should(have.text('mail@gmail.com'))
browser.element('#output #currentAddress').should(have.text('Russia'))
browser.element('#output #permanentAddress').should(have.text('Moscow'))