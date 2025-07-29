import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    courses_input = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_input).to_be_visible()
    expect(courses_input).to_have_text('Courses')

    results_courses_icon_input = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(results_courses_icon_input).to_be_visible()

    results_courses_title_input = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_courses_title_input).to_be_visible()
    expect(results_courses_title_input).to_have_text('There is no results')

    results_courses_description_input = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_courses_description_input).to_be_visible()
    expect(results_courses_description_input).to_have_text('Results from the load test pipeline will be displayed here')
