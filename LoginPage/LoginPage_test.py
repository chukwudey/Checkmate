import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LoginLocator.LoginLocator_test import LoginLocatorPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self,username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.PASSWORD))
        enter_password.send_keys(password)

    def enter_login_button(self):
        enter_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.LOGIN_BUTTON))
        enter_login_button.click()

    def error_message(self):
        error_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.ERROR))
        error_message.is_displayed()

        time.sleep(5)