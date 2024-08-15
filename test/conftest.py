import time
import pytest
from selenium import webdriver
from locators import SignInMain
from constants import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    def _auth(url, loc):
        driver.get(url)
        driver.find_element(*loc).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        time.sleep(1)
    return _auth
