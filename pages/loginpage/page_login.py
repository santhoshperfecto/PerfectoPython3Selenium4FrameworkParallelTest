from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):  # Inheriting SeleniumDriver class

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, reporting_client):
        super().__init__(driver, reporting_client)
        self.driver = driver
        self.reporting_client = reporting_client

    # Element locators
    emailField_XPATH = "//input[@name='login_email']"
    passwordField_XPATH = "//input[@name='login_password']"
    loginBtn_NAME = "login_login_btn"

    # Methods to find elements by locators
    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self.emailField_XPATH)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH, self.passwordField_XPATH)

    def getLoginBtn(self):
        return self.driver.find_element(By.NAME, self.loginBtn_NAME)

    # Methods to perform actions
    def enterEmail(self, email):
        self.sendKeys(email, self.emailField_XPATH, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self.passwordField_XPATH, locatorType="xpath")

    def clickLoginBtn(self):
        self.elementClick(self.loginBtn_NAME, locatorType="name")

    # Method with test steps
    def login(self, email, password):
        self.reporting_client.step_start("Enter email")
        self.enterEmail(email)

        self.reporting_client.step_start("Enter password")
        self.enterPassword(password)

        self.reporting_client.step_start("Click on Login")
        self.clickLoginBtn()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//ion-title[normalize-space()='Expenses']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self.emailField_XPATH,
                                       locatorType="xpath")
        return result

