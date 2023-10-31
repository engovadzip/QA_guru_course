import allure
from Homework_10.pages.registration_page_high import RegistrationPage
from Homework_10.users.users import User


@allure.step("Проверка формы регистрации")
def test_hw10():
    registration_page = RegistrationPage()
    user = User(
        last_name='Gazizov',
        first_name='Timir',
        email='my_mail@gmail.com',
        gender='Male',
        phone='9999999999',
        month_of_birth='June',
        year_of_birth='1994',
        day_of_birth='11',
        subject='Maths',
        hobby='Sports, Music',
        picture='picture.jpg',
        address='Shevchenko street',
        state='Haryana',
        city='Karnal'
    )

    registration_page.open_form()
    registration_page.register_user(user)
    registration_page.check_registration(user)