"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from perfecto import PerfectoExecutionContext, PerfectoReportiumClient
from perfecto import model


class WebDriverFactory:

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverReportingInstance(self):
        """
       Get WebDriver and Perfecto reporting Instance based on the browser configuration

        Returns:
            'WebDriver and Perfecto reporting Instance'
        """
        global driver
        cloudName = "demo"  # Ex - demo

        perfectoOptions = {
            'securityToken': '<Security Token>',
            'browserName': self.browser
        }

        if self.browser == "Safari":  # To run on macOS Monterey
            perfectoOptions['platformVersion'] = 'macOS Monterey'

        else:
            perfectoOptions['platformVersion'] = '11'  # To run on Windows 11

        baseURL = "http://expensetracker.perfectomobile.com"

        if self.browser == "Edge":
            # Set edge driver
            edge_options = EdgeOptions()
            edge_options.platform_name = "Windows"
            edge_options.browser_version = 'latest'
            edge_options.set_capability('perfecto:options', perfectoOptions)
            driver = webdriver.Remote('https://' + cloudName + '.perfectomobile.com/nexperience/perfectomobile/wd/hub',
                                      options=edge_options)

        elif self.browser == "Firefox":
            # Set FF driver
            firefox_options = FirefoxOptions()
            firefox_options.platform_name = "Windows"
            firefox_options.browser_version = 'latest'
            firefox_options.set_capability('perfecto:options', perfectoOptions)
            driver = webdriver.Remote('https://' + cloudName + '.perfectomobile.com/nexperience/perfectomobile/wd/hub',
                                      options=firefox_options)

        elif self.browser == "Chrome":
            # Set chrome driver
            chrome_options = ChromeOptions()
            chrome_options.platform_name = "Windows"
            chrome_options.browser_version = 'latest'
            chrome_options.set_capability('perfecto:options', perfectoOptions)
            driver = webdriver.Remote('https://' + cloudName + '.perfectomobile.com/nexperience/perfectomobile/wd/hub',
                                      options=chrome_options)

        elif self.browser == "Safari":
            # Set Safari driver
            safari_options = SafariOptions()
            safari_options.platform_name = "MAC"
            safari_options.browser_version = '15'
            safari_options.set_capability('perfecto:options', perfectoOptions)
            driver = webdriver.Remote('https://' + cloudName + '.perfectomobile.com/nexperience/perfectomobile/wd/hub',
                                      options=safari_options)

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()

        # Reporting client
        perfecto_execution_context = PerfectoExecutionContext(webdriver=driver,
                                                              tags=['Tag1', 'Tag2'],
                                                              job=model.Job('ExpenseJob', '1', 'MainBranch'),
                                                              project=model.Project('Expense', '1.0'))

        reporting_client = PerfectoReportiumClient(perfecto_execution_context)

        # Loading browser with App URL
        driver.get(baseURL)
        return driver, reporting_client
