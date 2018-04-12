from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        result = lp.verifyLoginSuccess()

        assert result == True
        driver.quit()
