import pytest
from locators import SignInMain
from constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignin:

    @pytest.mark.parametrize("url, submit_selector", [
        ("https://stellarburgers.nomoreparties.site/", SignInMain.SUBMIT_BUTTON),
        ("https://stellarburgers.nomoreparties.site/", SignInMain.SUBMIT_TEXT_LK),
        ("https://stellarburgers.nomoreparties.site/register", SignInMain.SUBMIT_LOGIN),
        ("https://stellarburgers.nomoreparties.site/forgot-password", SignInMain.SUBMIT_LOGIN)
    ])
    def test_signin(self, driver, auth, url, submit_selector):
        auth(url, submit_selector)

        driver.find_element(*SignInMain.SUBMIT_LK).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.PROFILE_LINK))
        name = driver.find_element(*SignInMain.CURR_NAME_DIS)
        value_attribute = name.get_attribute('value')
        assert value_attribute == name_const