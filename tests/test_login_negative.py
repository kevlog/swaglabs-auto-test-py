from pages.login_page import LoginPage
from utils.config import USERNAME, WRONGPASS

def test_login_wrong_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login(USERNAME, WRONGPASS)

    assert login.is_error_displayed()
