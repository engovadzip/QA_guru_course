from selene import browser, be, have
import resources



class RegistrationPage():
    def open_form(self):
        browser.open('/automation-practice-form')

    def register_user(self, user):
        browser.element('#firstName').send_keys(user.first_name)
        browser.element('#lastName').send_keys(user.last_name)
        browser.element('#userEmail').send_keys(user.email)

        user.gender = user.gender.capitalize()
        browser.element(f'//label[text() = "{user.gender}"]').click()
        browser.element('#userNumber').send_keys(user.phone)

        user.month_of_birth = user.month_of_birth.capitalize()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'//*[text()="{user.month_of_birth}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'//*[text()={user.year_of_birth}]').click()
        browser.element(f'//div[text()={user.day_of_birth}]').click()

        browser.element('#firstName').click()

        browser.element('#subjectsInput').type(f'{user.subject}').press_enter()

        browser.element('//label[@for="hobbies-checkbox-1"]').click()
        browser.element('//label[@for="hobbies-checkbox-3"]').click()

        browser.element('#uploadPicture').should(be.blank).send_keys(resources.path('picture.jpg'))

        browser.element('#currentAddress').send_keys(f'{user.address}')

        user.state = user.state.capitalize()
        browser.element('#state').click()
        browser.element(f'//*[text()="{user.state}"]').click()

        user.city = user.city.capitalize()
        browser.element('#city').click()
        browser.element(f'//*[text()="{user.city}"]').click()

        browser.element('#submit').click()

    def check_registration(self, user):
        full_name = f'{user.first_name} {user.last_name}'
        state_city = f'{user.state} {user.city}'
        date_of_birth = f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}'
        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                user.email,
                user.gender,
                user.phone,
                date_of_birth,
                user.subject,
                user.hobby,
                user.picture,
                user.address,
                state_city
            ))

        browser.element('#closeLargeModal').click()