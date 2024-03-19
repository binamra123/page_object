from selenium.webdriver.common.by import By

class LoginPageElements:

    USERNAME_TEXTBOX = (By.ID, "username")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@value='Login']")
    ERROR_MESSAGE = (By.XPATH, "//*[@class='form-error']")
    ERROR_USERNAME = (By.XPATH, "//*[contains(text(),'The username field is required.')]")
    ERROR_PASSWORD = (By.XPATH, "//*[contains(text(),'The password field is required.')]")
    CHECK_BOX = (By.CLASS_NAME,'checkmark')
