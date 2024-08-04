from selenium.webdriver.common.by import By


class LoginLocatorPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR = (By.ID, "errorMessage")