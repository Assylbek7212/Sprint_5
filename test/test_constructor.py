import pytest
from locators import SignInMain
from constants import name_site, active_tab_class


class TestConstructor:

    @pytest.fixture
    def navigate_to_home(self, driver, auth):
        auth(name_site, SignInMain.SUBMIT_BUTTON)
        yield

    def test_constructor_tab_buns(self, driver, navigate_to_home):
        step = driver.find_element(*SignInMain.BUNS_TEXT)
        step_class = step.get_attribute('class')
        assert step_class == active_tab_class, f"Expected '{active_tab_class}', but got '{step_class}'"

    @pytest.mark.parametrize("tab", [SignInMain.SAUCES_TEXT, SignInMain.FILLINGS_TEXT])
    def test_constructor_other_tabs(self, driver, navigate_to_home, tab):
        driver.find_element(*tab).click()
        step = driver.find_element(*tab)
        step_class = step.get_attribute('class')
        assert step_class == active_tab_class, f"Expected '{active_tab_class}', but got '{step_class}'"