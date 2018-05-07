from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import CoursesPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class RegisterTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.cp = CoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def testRegisterError(self):
        self.lp.login(
            "test@email.com", "abcabc")
        self.cp.registerClass(
            "JavaScript")
        result = self.cp.verifyErrorMessage()
        assert result == True
