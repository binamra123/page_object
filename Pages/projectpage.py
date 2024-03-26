from Utils.locators import  ProjectPageElements
from Utils.locators import LoginPageElements
from selenium.webdriver.common.action_chains import ActionChains


class ProjectPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*LoginPageElements.USERNAME_TEXTBOX).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageElements.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageElements.LOGIN_BUTTON).click()

    def search_field(self, search):
        self.driver.find_element(*ProjectPageElements.SEARCH_TEXTBOX).send_keys(search)
    
    def filter_box(self):
        self.driver.find_element(*ProjectPageElements.FILTER_FIELD).click()
         
    def import_project(self):
        self.driver.find_element(*ProjectPageElements.IMPORT_BUTTON).click()

    def add_project(self):
        self.driver.find_element(*ProjectPageElements.ADD_PROJECT).click()
    
    def nepali_con(self):
        self.driver.find_element(*ProjectPageElements.NEPALI_CONVERT).click()
    
    def english_con(self):
        self.driver.find_element(*ProjectPageElements.ENGLISH_CONVERT).click()
    
    def filter_button(self):
        self.driver.find_element(*ProjectPageElements.FILTER_OPTION).click()
    
    def radio_opt1(self):
        self.driver.find_element(*ProjectPageElements.RADIO1_OPTION).click()
    
    def radio_opt2(self):
        self.driver.find_element(*ProjectPageElements.RADIO2_OPTION).click()
    
    def radio_opt3(self):
        self.driver.find_element(*ProjectPageElements.RADIO3_OPTION).click()
    
    def radio_opt4(self):
        self.driver.find_element(*ProjectPageElements.RADIO4_OPTION).click()
    
    def project_social(self):
        self.driver.find_element(*ProjectPageElements.SOCIAL_OPTION).click()
    
    def nonexst_project(self):
        nonexstproject = self.driver.find_element(*ProjectPageElements.NON_PROJECT)
        return nonexstproject.text if nonexstproject else None
    
    def drag_and_drop(self):
        source = 'D:\QA Intern\page_object\IMSPom\TestData\sample-revised-project.xlsx'
        target = self.driver.find_element(*ProjectPageElements.DROP_FIELD)
        target.send_keys(source)

        