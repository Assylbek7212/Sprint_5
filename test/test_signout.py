from locators import SignInMain
from constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSignOut:
    def test_signout(self, driver, auth):
        auth(name_site, SignInMain.SUBMIT_BUTTON)

        driver.find_element(*SignInMain.SUBMIT_LK).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.SUBMIT_EXIT))
        driver.find_element(*SignInMain.SUBMIT_EXIT).click()
        time.sleep(3)
        url_before_click = driver.current_url
        driver.find_element(*SignInMain.SUBMIT_LK).click()
        url_after_click = driver.current_url

        assert url_before_click == url_after_click