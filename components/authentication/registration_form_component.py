from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'registration-form-email-input', 'Email')
        self.username_input = Input(page,'registration-form-username-input', 'Username')
        self.password_input = Input(page,'registration-form-password-input', 'Password')

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input.get_locator()).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input.get_locator()).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input.get_locator()).to_have_value(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input.get_locator()).to_be_visible()
        expect(self.email_input.get_locator()).to_have_value(email)

        expect(self.username_input.get_locator()).to_be_visible()
        expect(self.username_input.get_locator()).to_have_value(username)

        expect(self.password_input.get_locator()).to_be_visible()
        expect(self.password_input.get_locator()).to_have_value(password)