from base.basepage import BasePage
from utilities.util import Util
import utilities.custom_logger as cl
import logging


class CoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"  # id
    _search_button = "search-course-button"  # id
    _course = "course-listing"  # class
    _enroll_button = "enroll-button-top"  # id
    _cc_num = "credit-card-number"  # id
    _cc_exp = "expiration"  # id
    _cc_cvv = "cvc"  # id
    _postal = "postal"  # id
    _submit_enroll = "confirm-purchase"  # id
    _enroll_error_message = "cc_error"  # class

    # Credit info
    def getNums(self, num):
        return Util.getAlphaNumeric(length=num, type='digits')

    def searchCourse(self, course):
        self.sendKeys(course, self._search_box)
        self.elementClick(self._search_button)

    def selectCourse(self):
        self.elementClick(self._course, locatorType="class")

    def clickEnroll(self):
        self.elementClick(self._enroll_button)

    def scrollBottom(self):
        self.webScroll("down")

    def enterCreditInfo(self):
        ccNum = self.getNums(12)
        expNum = self.getNums(4)
        cvvNum = self.getNums(3)
        zipCode = self.getNums(5)
        self.sendKeys(ccNum, self._cc_num)
        self.sendKeys(expNum, self._cc_exp)
        self.sendKeys(cvvNum, self._cc_cvv)
        self.sendKeys(zipCode, self._postal)

    def submitEnroll(self):
        self.elementClick(self._submit_enroll)

    def registerClass(self, course="JavaScript"):
        self.searchCourse(course)
        self.selectCourse()
        self.clickEnroll()
        self.scrollBottom()
        self.enterCreditInfo()
        self.submitEnroll()

    def verifyErrorMessage(self):
        result = self.isElementPresent(
            self._enroll_error_message, "class")
        return result
