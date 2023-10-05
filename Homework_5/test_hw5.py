from selene import be, browser, have
import os
import time


def test_hw5():
    browser.open('/automation-practice-form')

    browser.element('//input[@placeholder="First Name"]').send_keys('Timir')
    browser.element('//input[@placeholder="Last Name"]').send_keys('Gazizov')
    browser.element('#userEmail').send_keys('my_mail@gmail.com')
    browser.element('//label[@for="gender-radio-1"]').click()
    browser.element('//input[@placeholder="Mobile Number"]').send_keys('9999999999')

    browser.element('#dateOfBirthInput').click()
    browser.element('//select[@class="react-datepicker__month-select"]').click()
    browser.element('//*[text()="June"]').click()

    browser.element('//select[@class="react-datepicker__year-select"]').click()
    browser.element('//*[text()="1994"]').click()
    browser.element('//div[text()="11"]').click()

    browser.element('//input[@placeholder="First Name"]').click()

    browser.element('#subjectsInput').type('math').press_enter()

    browser.element('//label[@for="hobbies-checkbox-1"]').click()
    browser.element('//label[@for="hobbies-checkbox-3"]').click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'picture.jpg')
    browser.element('#uploadPicture').should(be.blank).send_keys(file_path)

    browser.element('//textarea[@placeholder="Current Address"]').send_keys('Shevchenko street')

    browser.element('//div[text()="Select State"]').click()
    browser.element('//*[text()="Haryana"]').click()

    browser.element('//div[text()="Select City"]').click()
    browser.element('//*[text()="Karnal"]').click()

    browser.element('#submit').click()

    browser.element('//div[@class="modal-content"]').should(be.visible)
    browser.element('//div[text()="Thanks for submitting the form"]').should(be.visible)

    browser.element('//td[text()="my_mail@gmail.com"]').should(be.visible)
    browser.element('//td[text()="Male"]').should(be.visible)
    browser.element('//td[text()="9999999999"]').should(be.visible)
    browser.element('//td[contains(text(), "11 June") and contains(text(), "1994")]').should(be.visible)
    browser.element('//td[text()="Sports, Music"]').should(be.visible)
    browser.element('//td[text()="picture.jpg"]').should(be.visible)
    browser.element('//td[text()="Shevchenko street"]').should(be.visible)
    browser.element('//td[contains(text(), "Haryana") and contains(text(), "Karnal")]').should(be.visible)
    browser.element('//td[contains(text(), "Maths")]').should(be.visible)

    browser.element('#closeLargeModal').click()

    time.sleep(3)





