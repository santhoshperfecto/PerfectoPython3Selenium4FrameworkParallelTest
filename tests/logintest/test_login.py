import time
import pytest
from perfecto import TestResultFactory, TestContext
from pages.loginpage.page_login import LoginPage


@pytest.mark.usefixtures("setUp_module", "setUp_test")
class TestLogin:
    baseURL = "http://expensetracker.perfectomobile.com"

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp_module):
        self.lp = LoginPage(self.driver, self.reporting_client)

    @pytest.mark.run(order=2)
    def test_login(self):
        self.reporting_client.test_start('Expense Test login', TestContext(tags=['Demo']))
        self.reporting_client.step_start("Navigate to URL")
        self.driver.get(self.baseURL)
        self.reporting_client.step_end()
        self.lp.login("test@perfecto.com", "test123")
        time.sleep(4)
        result = self.lp.verifyLoginSuccessful()
        self.reporting_client.reportium_assert("Login successful", result == True)
        self.reporting_client.test_stop(TestResultFactory.create_success())
