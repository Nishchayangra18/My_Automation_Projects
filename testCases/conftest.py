import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


@pytest.fixture
def Setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser........")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


############################ Pytest HTML Report ######################################

# It is the hook to add Environment info to HTML Reports
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nop Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Nishchay"


# It is the hook to delete/modify Environment info to HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
