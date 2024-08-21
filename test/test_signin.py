import pytest
from locators import SignInMain, URLS
from constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignin:

    @pytest.mark.parametrize("url, submit_selector", [
        (URLS.STELLAR_BURGERS_HOME, SignInMain.SUBMIT_BUTTON),
        (URLS.STELLAR_BURGERS_HOME, SignInMain.SUBMIT_TEXT_LK),
        (URLS.STELLAR_BURGERS_REGISTER, SignInMain.SUBMIT_LOGIN),
        (URLS.STELLAR_BURGERS_FORGOT_PASSWORD, SignInMain.SUBMIT_LOGIN)
    ])
    def test_signin(self, driver, auth, url, submit_selector):
        auth(url, submit_selector)

        driver.find_element(*SignInMain.SUBMIT_LK).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.PROFILE_LINK))
        name = driver.find_element(*SignInMain.CURR_NAME_DIS)
        value_attribute = name.get_attribute('value')
        assert value_attribute == name_const