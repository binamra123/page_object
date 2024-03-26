import pytest
import time
from Utils.driver import get_driver
from Utils.Urlconfig import URLConfig
from Pages.loginpage import LoginPage
from Pages.projectpage import ProjectPage
from Utils.locators import LoginPageElements
from Utils.locators import ProjectPageElements
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


# def test_exstname(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
#     assert driver.title == "Projects | Infrastructure Management System Stage"
#     project_page.search_field("test")


# def test_nonexstname(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
#     assert driver.title == "Projects | Infrastructure Management System Stage"
#     project_page.search_field("abcd")
#     message1 = project_page.nonexst_project()
#     assert message1 == "Sorry we could not find any project", f"Unexpected error message: {message1}"


# def test_engtonep(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
#     assert driver.title == "Projects | Infrastructure Management System Stage"
#     time.sleep(2)
#     project_page.english_con()
#     project_page.search_field("abcd")
#     nepali = ProjectPageElements.NEPALI_CONVERT
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((nepali)))
#     project_page.nepali_con()
#     title_text_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProjectPageElements.TITLE_TEXT))
#     gettext = title_text_element.text
#     assert gettext == 'पूर्वाधार व्यवस्थापन प्रणाली'


# def test_addproject(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects | Infrastructure Management System Stage"))
#     assert driver.title == "Projects | Infrastructure Management System Stage"
#     project_page.add_project()
    

# def test_importproject(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     project_page.import_project()
#     WebDriverWait(driver, 10).until(EC.title_contains("Projects Import | Infrastructure Management System Stage"))
#     assert driver.title == "Projects Import | Infrastructure Management System Stage"


# def test_socialproject(setup):
#     project_page = ProjectPage(driver)
#     project_page.open_page(URLConfig.LOGIN_PAGE_URL)
#     project_page.enter_username(data['valid_name'])
#     project_page.enter_password(data['valid_pass'])
#     project_page.click_login()
#     time.sleep(2)
#     social = ProjectPageElements.SOCIAL_OPTION
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((social)))
#     project_page.project_social()

def test_importanddragproject(setup):
    project_page = ProjectPage(driver)
    project_page.open_page(URLConfig.LOGIN_PAGE_URL)
    project_page.enter_username(data['valid_name'])
    project_page.enter_password(data['valid_pass'])
    project_page.click_login()
    project_page.import_project()
    time.sleep(2)
    project_page.drag_and_drop()