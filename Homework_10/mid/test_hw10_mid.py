import allure
import time

from Homework_10.mid.pages.registration_page_mid import RegistrationPage


@allure.step("Проверка формы регистрации")
def test_hw10():
    registration_page = RegistrationPage()

    registration_page.open_form()

    registration_page.fill_first_name('Timir')
    registration_page.fill_last_name('Gazizov')
    registration_page.fill_email('my_mail@gmail.com')
    registration_page.select_gender('male')
    registration_page.fill_phone_number('9999999999')
    registration_page.select_date_of_birth('june', 11, 1994)
    registration_page.select_subject('math')
    registration_page.select_hobbies()
    registration_page.upload_picture()
    registration_page.fill_address('Shevchenko street')
    registration_page.select_state("Haryana")
    registration_page.select_city("Karnal")

    registration_page.submit_button_click()

    registration_page.should_registered_user_with('Timir Gazizov', 'my_mail@gmail.com', 'Male',
                                                  '9999999999', '11 June,1994', 'Maths',
                                                  'Sports, Music', 'picture.jpg', 'Shevchenko street',
                                                  'Haryana Karnal')

    time.sleep(3)