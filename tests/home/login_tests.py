from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest():

    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(baseUrl)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

