from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class CoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    