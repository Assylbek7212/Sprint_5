from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from locators import *
from constants import *

class TestRegistration:
    def test_registration(self, driver):
        driver.get(reg_site)

        random_login = generate_random_login()
        random_password = generate_random_password()
        random_name = generate_random_name()

        name_field = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_field.send_keys(random_name)
        email_field.send_keys(random_login)
        password_field.send_keys(random_password)

        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.SUBMIT_BUTTON_SIGN_IN))

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(SignInMain.CURR_NAME123))

        name = driver.find_element(*SignInMain.CURR_NAME123)
        driver.find_element(*SignInMain.CURR_NAME123).send_keys(random_name)
        value_attribute = name.get_attribute('value')

        assert value_attribute == random_name

    def test_registration_with_short_password(self, driver):
        driver.get(reg_site)

        random_login = generate_random_login()
        random_name = generate_random_name()

        name_field = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_field.send_keys(random_name)
        email_field.send_keys(random_login)
        password_field.send_keys("123")

        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )

        assert "Некорректный пароль" in error_message.text