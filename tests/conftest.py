import pytest
from base.webdriverfactory import WebDriverFactory


# Setup method which runs one time before/after each module(test_*.py).
@pytest.fixture(scope="class", params=["Edge", "Chrome", "Firefox", "Safari"]) # To run test parallely
def setUp_module(request):  # Fixtures to get command line arguments
    wdf = WebDriverFactory(request.param)
    driver, reporting_client = wdf.getWebDriverReportingInstance()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.reporting_client = reporting_client

    yield driver, reporting_client
    driver.quit()


@pytest.fixture()  # Setup method which runs before/after each test methods,fixture default scope is method
def setUp_test():  # It does nothing now, can be used in future
    print("Running before every test method")

    yield
    print("Running after each test method")
