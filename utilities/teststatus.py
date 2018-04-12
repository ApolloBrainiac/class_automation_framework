"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import customLogger


class TestStatus(SeleniumDriver):

        log = cl.customLogger(logging.INFO)

        def __init__(self, driver):
            """
            Inits CheckPoint class
            """
            super(TestStatus, self).__init__(driver)
            self.resultList = []

        def setResult(self, result, resultMessage):
            print()

        def mark(self, testName, result, resultMessage):
            """
            Mark the result of the verification point in a test case
            """
            print()

        def markFinal(self, testName, result, resultMessage):
            """
            Mark the final result of the verification point in a test case
            This needs to be called at least once in a test case
            This should be final test status of the test case
            """
            print()