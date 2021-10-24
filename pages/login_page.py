from playwright.sync_api._generated import ElementHandle

from pages.base_page import BasePage


class LoginPage(BasePage):
    @property
    def password_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("input[data-e2e='password']")

    @property
    def submit_button(self) -> ElementHandle:
        return self.userform.wait_for_selector("button[data-e2e='login']")

    @property
    def userform(self) -> ElementHandle:
        return self.page.wait_for_selector("#userForm")

    @property
    def username_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("input[data-e2e='username']")

    def fill_form(self) -> None:
        """Fill out the login form.

        :param user: A user intended for login.
        """
        self.username_field.fill('testuser01@gmail.com')
        self.password_field.fill('test123456')

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")