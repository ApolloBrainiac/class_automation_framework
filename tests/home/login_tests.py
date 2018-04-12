from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTest(unittest.TestCase):
    baseUrl = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)
    lp = LoginPage(driver)

    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccess()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseUrl)
        self.lp.login("test@email.com", "incorrect")
        result = self.lp.verifyLoginFail()
        assert result == True
