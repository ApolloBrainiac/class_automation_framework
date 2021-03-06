from pages.home.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login(
            "test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(
            result1, 'Title verified')
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal(
            "test_validLogin", result2, 'Login was successful')

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(
            "test@email.com", "incorrect")
        result = self.lp.verifyLoginFail()
        assert result == True
