from selenium.webdriver.common.by import By

class LoginPageElements:

    USERNAME_TEXTBOX = (By.ID, "username")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@value='Login']")
    ERROR_MESSAGE = (By.XPATH, "//*[@class='form-error']")
    ERROR_USERNAME = (By.XPATH, "//*[contains(text(),'The username field is required.')]")
    ERROR_PASSWORD = (By.XPATH, "//*[contains(text(),'The password field is required.')]")
    CHECK_BOX = (By.CLASS_NAME,'checkmark')

class ProjectPageElements:

    SEARCH_TEXTBOX = (By.ID, "project-title")
    FILTER_FIELD = (By.XPATH, "//span[text()='Filters']")
    IMPORT_BUTTON = (By.XPATH, '//*[contains(@href,"/projects/import")]')
    ADD_PROJECT = (By.XPATH, '//*[contains(@href,"/projects/create")]')
    NEPALI_CONVERT = (By.XPATH, "//span[text()='ने']")
    ENGLISH_CONVERT = (By.XPATH, "//span[text()='en']")
    FILTER_OPTION = (By.XPATH,'//*[@class="trigger"]')
    RADIO1_OPTION = (By.XPATH,'//input[@value="pipeline"]')
    RADIO2_OPTION = (By.XPATH,'//input[@value="implementation"]')
    RADIO3_OPTION = (By.XPATH,'//input[@value="completion"]')
    RADIO4_OPTION = (By.XPATH,'//input[@value="cancelled"]')
    SOCIAL_OPTION = (By.XPATH,"//*[contains(text(),'Social')]")
    NON_PROJECT = (By.XPATH,"//*[@class='data-not-available']")
    TITLE_TEXT = (By.XPATH,"//*[@class='app-name']")
    DROP_FIELD = (By.XPATH,"//*[@id='file']")
        





        