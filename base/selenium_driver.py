from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
from perfecto import TestResultFactory


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, reporting_client):
        self.driver = driver
        self.reporting_client = reporting_client

    def exceptiondriverQuit(self):
        self.reporting_client.test_stop(TestResultFactory.create_failure("Please check message on failed step"))
        self.driver.quit()

    # Custom/user defined methods for Selenium actions
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
            self.exceptiondriverQuit()

        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
            self.exceptiondriverQuit()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()
            self.exceptiondriverQuit()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.error("Element not found")
            self.exceptiondriverQuit()

            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.error("Element not found")
            self.exceptiondriverQuit()

            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
            self.exceptiondriverQuit()

            return element
