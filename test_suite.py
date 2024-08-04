import time

import pytest
from selenium import webdriver

from LoginPage.LoginPage_test import LoginPage


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("#")
    return login_page


time.sleep(5)


def test_login_page(login):
    login.enter_username("username")
    login.enter_password("password")
    login.enter_login_button()


def test_fail_login_page(login):
    login.enter_username("invalidUsername")
    login.enter_password("invalidPassword")
    login.enter_login_button()
    assert test_login_page == test_fail_login_page, "error--invalid credentials"
