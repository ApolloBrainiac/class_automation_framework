from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest():

    def test_validLogin(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(baseUrl)

        loginLink = driver.find_element(
            By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = driver.find_element(
            By.ID, "user_email")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element(
            By.ID, "user_password")
        passwordField.send_keys("abcabc")

        loginButton = driver.find_element(
            By.NAME, "commit")
        loginButton.click()

        userIcon = driver.find_element(
            By.XPATH, ".//*[id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login failed")


lt = LoginTest()
lt.test_validLogin()
