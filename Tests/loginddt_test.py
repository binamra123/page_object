import pytest
import time
from Utils.driver import get_driver
from Utils.Urlconfig import URLConfig
from Pages.loginpage import LoginPage
from Utils.data_ddt import read_data
from Utils.data_ddt import readData
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
    driver.close()

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

# @pytest.mark.parametrize("username, password", read_data())
# def test_excellogin(setup, username, password):
#     driver = setup
#     login_page = LoginPage(driver)
#     login_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     login_page.enter_username(username)
#     login_page.enter_password(password)
#     login_page.click_login()
#     assert driver.title == "Projects | Infrastructure Management System Stage"


@pytest.mark.parametrize("username, password", readData())
def test_csvlogin(setup, username, password):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    assert driver.title == "Projects | Infrastructure Management System Stage"


