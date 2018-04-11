from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import time


class LoginTest(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        time.sleep(3)

        userIcon = driver.find_element(
            By.XPATH, "//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")


lt = LoginTest()
lt.test_validLogin()
