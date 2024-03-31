import time

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

from Pages.Login_Page import LoginPage
from utilities import XLUtils


@pytest.fixture(scope="class")
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


@pytest.fixture(scope="class")
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


############################ Pytest HTML Report ######################################

# It is the hook to add Environment info to HTML Reports
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "OrangeHRM"
    config.stash[metadata_key]["Module Name"] = "PIM"
    config.stash[metadata_key]["Tester"] = "Nishchay"


# It is the hook to delete/modify Environment info to HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


def processRowData(data):
    print("Processing Row Data:")
    for index, value in enumerate(data):
        print(f"Column {index + 1}: {value}")


@pytest.fixture(scope="class")
def test_Login_ddt(Setup):
    path = ".//testData/OrangeHRM_Testdata.xlsx"
    driver = Setup
    driver.maximize_window()
    lp = LoginPage(driver)

    rows = XLUtils.getRowCount(path, 'Login')
    print("Number of rows in excel", rows)
    colums = XLUtils.getColumnCount(path, 'Login')
    print("Number of colms in excel", colums)
    user = XLUtils.readData(path, 'Login', 2, 1)
    driver.get(user)

    for r in range(2, rows + 1):
        data = []
        for c in range(1, colums + 1):
            cell_data = XLUtils.readData(path, 'Login', r, c)
            exp = XLUtils.readData(path, 'Login', r, c + 3)
            data.append(cell_data)

        processRowData(data)

        lp.enterUsername(data[1])
        lp.enterPassword(data[2])
        lp.clickLogin()
        time.sleep(5)
