import time

import pytest
from selenium import webdriver
from Pages.Login_Page import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils


def processRowData(data):
    print("Processing Row Data:")
    for index, value in enumerate(data):
        print(f"Column {index + 1}: {value}")


class Test_001_Login:
    path = ".//testData/OrangeHRM_Testdata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.fixture
    def test_Login_ddt(self, Setup):
        self.logger.info("********************** Test_001_Login  ************************")
        self.logger.info("********************** Verifying Login Test  ************************")
        self.driver = Setup
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Login')
        print("Number of rows in excel", self.rows)
        self.colums = XLUtils.getColumnCount(self.path, 'Login')
        print("Number of colms in excel", self.colums)
        self.user = XLUtils.readData(self.path, 'Login', 2, 1)
        self.driver.get(self.user)

        list_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            data = []
            for c in range(1, self.colums + 1):
                cell_data = XLUtils.readData(self.path, 'Login', r, c)
                # self.user = XLUtils.readData(self.path, 'Login', r, c)
                # self.password = XLUtils.readData(self.path, 'Login', r, c)
                self.exp = XLUtils.readData(self.path, 'Login', r, c+3)
                data.append(cell_data)

            processRowData(data)

            self.lp.enterUsername(data[1])
            self.lp.enterPassword(data[2])
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = self.exp

            if act_title == exp_title:
                self.logger.info("***** Login test case Passed *****")
                self.lp.clickuserdropdown()
                self.lp.clickLogout()
            else:
                self.logger.info("***** Login test case Failed *****")
                self.lp.clickuserdropdown()
                self.lp.clickLogout()

        self.logger.info("********************** End of Login Test  ************************")
        self.logger.info("********************** Completed Test_001_Login ************************")
