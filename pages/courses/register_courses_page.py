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
    _course = "course-listing" #class
    _all_courses = "All Courses" #link text
    _enroll_button = "enroll-button-top" #id
    _cc_num = "credit-card-number" #id
    _cc_exp = "expiration" #id
    _cc_cvv = "cvc" #id
    _submit_enroll = "confirm-purchase" #id 
    _enroll_error_message = "cc_error" #class

