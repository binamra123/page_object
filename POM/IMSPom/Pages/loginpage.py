from Utils.locators import LoginPageElements
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
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
    
    def click_checkmark(self):
        checkbox_element  = self.driver.find_element(*LoginPageElements.CHECK_BOX)
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox_element).click().perform()

    def get_error_message(self):
        error_element = self.driver.find_element(*LoginPageElements.ERROR_MESSAGE)
        return error_element.text if error_element else None
    
    def get_error_username(self):
        error_element1 = self.driver.find_element(*LoginPageElements.ERROR_USERNAME)
        return error_element1.text if error_element1 else None
    
    def get_error_password(self):
        error_element2 = self.driver.find_element(*LoginPageElements.ERROR_PASSWORD)
        return error_element2.text if error_element2 else None
