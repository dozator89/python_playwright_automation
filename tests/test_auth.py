import pytest
from pages.main_page import Main
class Auth:
    USERNAME_INPUT = "[data-test = 'username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BTN = "[data-test='login-button']"

@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()