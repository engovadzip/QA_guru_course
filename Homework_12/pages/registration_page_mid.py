from selene import browser, be, have
import os


class RegistrationPage():
    def open_form(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, name):
        browser.element('//input[@placeholder="First Name"]').send_keys(name)

    def fill_last_name(self, last_name):
        browser.element('//input[@placeholder="Last Name"]').send_keys(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').send_keys(email)

    def select_gender(self, gender):
        gender = gender.capitalize()
        browser.element(f'//label[text() = "{gender}"]').click()

    def fill_phone_number(self, phone):
        browser.element('//input[@placeholder="Mobile Number"]').send_keys(phone)

    def select_date_of_birth(self, month, day, year):
        month = month.capitalize()
        browser.element('#dateOfBirthInput').click()
        browser.element('//select[@class="react-datepicker__month-select"]').click()
        browser.element(f'//*[text()="{month}"]').click()

        browser.element('//select[@class="react-datepicker__year-select"]').click()
        browser.element(f'//*[text()={year}]').click()
        browser.element(f'//div[text()={day}]').click()

        browser.element('//input[@placeholder="First Name"]').click()

    def select_subject(self, subject):
        browser.element('#subjectsInput').type(f'{subject}').press_enter()

    def select_hobbies(self):
        browser.element('//label[@for="hobbies-checkbox-1"]').click()
        browser.element('//label[@for="hobbies-checkbox-3"]').click()

    def upload_picture(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'picture.jpg')
        browser.element('#uploadPicture').should(be.blank).send_keys(file_path)

    def fill_address(self, address):
        browser.element('//textarea[@placeholder="Current Address"]').send_keys(f'{address}')

    def select_state(self, state):
        state = state.capitalize()
        browser.element('//div[text()="Select State"]').click()
        browser.element(f'//*[text()="{state}"]').click()

    def select_city(self, city):
        city = city.capitalize()
        browser.element('//div[text()="Select City"]').click()
        browser.element(f'//*[text()="{city}"]').click()

    def submit_button_click(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth,
                                    subject, hobbies, file, address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobbies,
                file,
                address,
                state_city,
            )
        )

        browser.element('#closeLargeModal').click()