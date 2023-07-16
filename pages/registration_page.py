import os
from selene import browser, have, command

from tests.conftest import path


class RegistrationPage:
    def __init__(self):
        self.should_registered_user_with = browser.element('.table').all('td').even

    def open_practice_form_page(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.element('label[for="gender-radio-1"]').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('[class="react-datepicker__year-select"]').type(year)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self):
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-2"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()

    def upload_image(self, file):
        browser.element('#uploadPicture').send_keys(path(file))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').click().press_enter()