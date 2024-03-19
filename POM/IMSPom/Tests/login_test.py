import pytest
import time
from Utils.driver import get_driver
from Utils.Urlconfig import URLConfig
from Pages.loginpage import LoginPage
from TestData.test_data import data

@pytest.fixture(params=["chrome"])
def browser(request):
    return request.param

@pytest.fixture
def setup(browser):
 global driver
 driver = get_driver(browser)
 yield driver
 driver.close()

def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['valid_name'])
    login_page.enter_password(data['valid_pass'])
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)
    assert driver.title == "Projects | Infrastructure Management System Stage"

def test_invalogin(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['invalid_name'])
    login_page.enter_password(data['invalid_pass'])
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

    error_message = login_page.get_error_message()
    assert error_message == "These credentials do not match our records.", f"Unexpected error message: {error_message}"

def test_invname(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['invalid_name'])
    login_page.enter_password(data['valid_pass'])
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

    error_message = login_page.get_error_message()
    assert error_message == "These credentials do not match our records.", f"Unexpected error message: {error_message}"

def test_invpass(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['valid_name'])
    login_page.enter_password(data['invalid_pass'])
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

    error_message = login_page.get_error_message()
    assert error_message == "These credentials do not match our records.", f"Unexpected error message: {error_message}"

def test_remember(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(data['valid_name'])
    login_page.enter_password(data['valid_pass'])
    time.sleep(2)
    login_page.click_checkmark()
    login_page.click_login()
    time.sleep(5)

def test_space(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(" ")
    login_page.enter_password(" ")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

    error_message1 = login_page.get_error_username()
    assert error_message1 == "The username field is required.", f"Unexpected error message: {error_message1}"
    error_message2 = login_page.get_error_password()
    assert error_message2 == "The password field is required.", f"Unexpected error message: {error_message2}"

def test_blankcred(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("")
    login_page.enter_password("")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

    error_message1 = login_page.get_error_username()
    assert error_message1 == "The username field is required.", f"Unexpected error message: {error_message1}"
    error_message2 = login_page.get_error_password()
    assert error_message2 == "The password field is required.", f"Unexpected error message: {error_message2}"

   

