from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD
def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login(USERNAME,PASSWORD)

    assert "inventory" in driver.current_url
