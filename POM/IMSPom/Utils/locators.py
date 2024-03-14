from selenium.webdriver.common.by import By

class LoginPageElements:

    USERNAME_TEXTBOX = (By.ID, "username")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-form"]/div/div[2]/div[4]/input')
