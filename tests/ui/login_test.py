import pytest
from playwright.sync_api import Page

from pages import LoginPage

@pytest.mark.login
def test_valid_login(page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.fill_form()
        login_page.submit_button.click()