import pytest
import time
from Utils.driver import get_driver
from Utils.Urlconfig import URLConfig
from Pages.loginpage import LoginPage

@pytest.fixture(params=["chrome"])
def browser(request):
    return request.param

@pytest.fixture
def setup(browser):
    global driver
    driver = get_driver(browser)
    yield
    driver.quit()

def test_login(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)
    assert driver.title == "Projects | Infrastructure Management System Stage"

def test_invalogin(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("admin")
    login_page.enter_password("abcd")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

def test_invname(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("admin")
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

def test_invpass(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("abcd")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

def test_remember(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("admin.dhangadhi")
    login_page.enter_password("password")
    time.sleep(2)
    checkbox = driver.find_element(By.CLASS_NAME, value='checkmark')
    ActionChains(driver).move_to_element(checkbox).click().perform()
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

def test_blankcred(setup):
    login_page = LoginPage(driver)
    login_page.open_page(URLConfig.LOGIN_PAGE_URL)
    login_page.enter_username("")
    login_page.enter_password("")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)

