import pytest
import time
from Utils.driver import get_driver
from Utils.Urlconfig import URLConfig
from Pages.loginpage import LoginPage
from Utils.locators import LoginPageElements
from TestData.test_data import data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(params=["chrome"])
def browser(request):
    return request.param

@pytest.fixture
def setup(browser):
 global driver
 driver = get_driver(browser)
 yield driver
 time.sleep(4)
 driver.close()


def test_login(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['valid_name'])
    login_page.enter_password(data['valid_pass'])
    login_page.click_login()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
    assert driver.title == "Projects | Infrastructure Management System Stage"


# def test_invname(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username(data['invalid_name'])
#     login_page.enter_password(data['valid_pass'])
#     login_page.click_login()
#     error_message_locator = LoginPageElements.ERROR_MESSAGE
#     error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator)).text
#     expected_error_message = "These credentials do not match our records."
#     assert error_message == expected_error_message, f"Unexpected error message: {error_message}"
   

# def test_invpass(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username(data['valid_name'])
#     login_page.enter_password(data['invalid_pass'])
#     login_page.click_login()
#     error_message_locator = LoginPageElements.ERROR_MESSAGE
#     error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator)).text
#     expected_error_message = "These credentials do not match our records."
#     assert error_message == expected_error_message, f"Unexpected error message: {error_message}"

# # def test_remember(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username(data['valid_name'])
#     login_page.enter_password(data['valid_pass'])
#     login_page.click_checkmark()
#     login_page.click_login()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
#     assert driver.title == "Projects | Infrastructure Management System Stage"

# def test_space(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username(" ")
#     login_page.enter_password(" ")
#     login_page.click_login()

#     error_message1 = login_page.get_error_username()
#     assert error_message1 == "The username field is required.", f"Unexpected error message: {error_message1}"
#     error_message2 = login_page.get_error_password()
#     assert error_message2 == "The password field is required.", f"Unexpected error message: {error_message2}"

# def test_blankcred(setup):
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username("")
#     login_page.enter_password("")
#     login_page.click_login()

#     error_message1 = login_page.get_error_username()
#     assert error_message1 == "The username field is required.", f"Unexpected error message: {error_message1}"
#     error_message2 = login_page.get_error_password()
#     assert error_message2 == "The password field is required.", f"Unexpected error message: {error_message2}"

   
