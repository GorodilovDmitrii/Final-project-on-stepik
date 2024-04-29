from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url(), "This is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_email), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.registration_email), "Registration form is not presented"
