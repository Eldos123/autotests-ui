import pytest
from playwright.sync_api import sync_playwright

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit_registration_page("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form_input(email="user@gmail.com", username="username", password="password")
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()

