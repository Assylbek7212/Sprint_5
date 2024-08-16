import time
import pytest
from selenium import webdriver
from locators import SignInMain
from constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.SAUCES_TEXT))

    return _auth
