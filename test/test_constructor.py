import time

import pytest
from locators import SignInMain
from constants import name_site, active_tab_class

class TestConstructor:
    @pytest.mark.parametrize("tab",
                             [SignInMain.SAUCES_TEXT,
                              SignInMain.FILLINGS_TEXT,
                              SignInMain.BUNS_TEXT])
    def test_constructor_tab(self, driver, auth, tab):
        auth(name_site, SignInMain.SUBMIT_BUTTON)

        if tab == SignInMain.BUNS_TEXT:
            step = driver.find_element(*tab)
            step_class = step.get_attribute('class')
            assert step_class == active_tab_class, f"Expected '{active_tab_class}', but got '{step_class}'"
        else:
            driver.find_element(*tab).click()

            step = driver.find_element(*tab)
            step_class = step.get_attribute('class')
            assert step_class == active_tab_class, f"Expected '{active_tab_class}', but got '{step_class}'"
