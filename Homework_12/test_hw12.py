import allure
import time

from pages.registration_page_mid import RegistrationPage


def test_hw11():
    registration_page = RegistrationPage()

    with allure.step('Открываем форму регистрации'):
        registration_page.open_form()

    with allure.step('Ввод имени и фамилии'):
        registration_page.fill_first_name('Timir')
        registration_page.fill_last_name('Gazizov')

    with allure.step('Ввод электронного адреса и номер телефона'):
        registration_page.fill_email('my_mail@gmail.com')
        registration_page.fill_phone_number('9999999999')

    with allure.step('Выбор пола'):
        registration_page.select_gender('male')

    with allure.step('Выбор дня рождения'):
        registration_page.select_date_of_birth('june', 11, 1994)

    with allure.step('Выбор предметов и увлечений'):
        registration_page.select_subject('math')
        registration_page.select_hobbies()

    with allure.step('Загрузка фотографии'):
        registration_page.upload_picture()

    with allure.step('Ввод адреса'):
        registration_page.fill_address('Shevchenko street')
        registration_page.select_state("Haryana")
        registration_page.select_city("Karnal")

    with allure.step('Нажатие "Submit"'):
        registration_page.submit_button_click()

    with allure.step('Проверка введенных данных'):
        registration_page.should_registered_user_with('Timir Gazizov', 'my_mail@gmail.com', 'Male',
                                                      '9999999999', '11 June,1994', 'Maths',
                                                      'Sports, Music', 'picture.jpg', 'Shevchenko street',
                                                      'Haryana Karnal')

    time.sleep(3)