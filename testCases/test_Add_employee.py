import os.path
import time


import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Login_Page import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
from Pages.Dashboard_Page import DashboardPage
from Pages.PIM_Page import PIMPage
from pynput.keyboard import Key, Controller


def processRowData(data):
    print("Processing Row Data:")
    for index, value in enumerate(data):
        print(f"Column {index + 1}: {value}")


class Test_002_Add_Employee:
    path = ".//testData/OrangeHRM_Testdata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_ddt(self, Setup):
        self.logger.info("********************** Test_002_Add_Employee  ************************")
        self.logger.info("********************** Verifying Add Employee Test  ************************")
        self.driver = Setup
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows_login = XLUtils.getRowCount(self.path, 'Login')
        self.columns_login = XLUtils.getColumnCount(self.path, 'Login')
        self.user = XLUtils.readData(self.path, 'Login', 2, 1)
        self.driver.get(self.user)

        for r in range(2, self.rows_login + 1):
            data = []
            for c in range(1, self.columns_login + 1):
                cell_data = XLUtils.readData(self.path, 'Login', r, c)
                self.exp = XLUtils.readData(self.path, 'Login', r, c+3)
                data.append(cell_data)

            processRowData(data)

            self.lp.enterUsername(data[1])
            self.lp.enterPassword(data[2])
            self.lp.clickLogin()
            time.sleep(5)

            self.dp = DashboardPage(self.driver)
            self.dp.clickPIM()

            self.pp = PIMPage(self.driver)
            self.pp.clickaddbutton()

            self.rows_add_employee = XLUtils.getRowCount(self.path, 'PIM_Add_Employee')
            self.columns_add_employee = XLUtils.getColumnCount(self.path, 'PIM_Add_Employee')

            for r in range(2, self.rows_add_employee + 1):
                data = []
                for c in range(1, self.columns_add_employee + 1):
                    cell_data = XLUtils.readData(self.path, 'PIM_Add_Employee', r, c)
                    data.append(cell_data)

                processRowData(data)
                # print(self.pp.enterfirstname(data[0]))
                # print(self.pp.entermiddlename(data[1]))
                # print(self.pp.enterlastname(data[2]))
                self.fullname = self.pp.enterfirstname(data[0]) + " " + self.pp.entermiddlename(data[1]) + " " + self.pp.enterlastname(data[2])
                print("fullname: " + self.fullname)
                self.pp.enteremployeeid(data[3])
                self.pp.clickCreateLoginSlideButton()
                self.pp.enterCreateLoginUsername(data[4])
                self.pp.enterCreateLoginPassword(data[5])
                self.pp.enterCreateLoginConfirmPassword(data[6])
                time.sleep(5)
                self.pp.addProfilePhoto()

                self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
                self.slash = "\\"
                self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
                self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
                print(self.dp_jpg_path)
                time.sleep(5)

                try:
                    keyword = Controller()
                    keyword.type(self.dp_jpg_path)
                    keyword.press(Key.enter)
                    keyword.release(Key.enter)
                    time.sleep(5)
                except Exception as e:
                    print(f"An error occurred: {e}")

                self.pp.clickSavebutton()
                time.sleep(5)
                # self.dp.clickPIM()
                self.pp.clickEmployeeList()
                time.sleep(5)
                self.pp.enterEmployeename(self.fullname)
                self.pp.clickSearchbutton()

                time.sleep(2)
                self.pp.verifyEmployeenameTable(self.fullname)
                # self.pp.enterEmployeename(self.fullname)
                # self.pp.clickSearchbutton()
                # self.pp.verifyEmployeenameTable(self.fullname)

                # try:
                #     self.pp.WaitForSuccessToaster()
                #     self.pp.GetTextSuccessToastMessage("Success")
                # except Exception as e:
                #     print(f"An error occurred: {e}")
                #
                # try:
                #     WebDriverWait(self.driver, 10).until(
                #         EC.url_changes("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
                #     )
                # except Exception as e:
                #     print(f"An error occurred: {e}")
                # self.pp.GetTextFullName(self.fullname)
                # time.sleep(3)


        self.logger.info("********************** End of Login Test  ************************")
        self.logger.info("********************** Completed Test_001_Login ************************")
