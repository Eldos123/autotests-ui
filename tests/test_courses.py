from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill("user.name@gmail.com")

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill("username")

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill("password")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        dashboard_input = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_input).to_be_visible()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_input = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_input).to_be_visible()
        expect(courses_input).to_have_text('Courses')

        results_courses_icon_input = page.get_by_test_id('courses-list-empty-view-icon')
        expect(results_courses_icon_input).to_be_visible()

        results_courses_title_input = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(results_courses_title_input).to_be_visible()
        expect(results_courses_title_input).to_have_text('There is no results')

        results_courses_description_input = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_courses_description_input).to_be_visible()
        expect(results_courses_description_input).to_have_text('Results from the load test pipeline will be displayed here')
