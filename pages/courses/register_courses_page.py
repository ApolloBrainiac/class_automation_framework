from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class CoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses" #id
    _search_button = "search-course-button" #id
    _course = "course-listing" #class
    _all_courses = "All Courses" #link text
    _enroll_button = "enroll-button-top" #id
    _cc_num = "credit-card-number" #id
    _cc_exp = "expiration" #id
    _cc_cvv = "cvc" #id
    _postal = "postal" #id
    _submit_enroll = "confirm-purchase" #id 
    _enroll_error_message = "cc_error" #class

    def searchCourse(self, course):
        self.sendKeys(course, self._search_box)
        self.elementClick(self._search_button)

    def selectCourse(self):
        self.elementClick(_course, locatorType="class")

    def clickEnroll(self):
        self.elementClick(_enroll_button)

    def scrollBottom(self):
        self.webScroll("down")

    def enterCreditInfo(self, ccNum, expNum, cvvNum, postal):
        self.sendKeys(ccNum, self._cc_num)
        self.sendKeys(expNum, self._cc_exp)
        self.sendKeys(cvvNum, self._cc_cvv)
        self.sendKeys(postal, self._postal)
        
    def submitEnroll(self):
        self.elementClick(_submit_enroll)

    def registerClass(self):
        self.searchCourse(course)
        self.selectCourse()
        self.clickEnroll()
        self.scrollBottom()
        self.enterCreditInfo(
            ccNum, expNum, cvvNum, postal)
        self.submitEnroll()

    def verifyError(self):
        result = self.isElementPresent(
            self._enroll_error_message, "class")
        return result