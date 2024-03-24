import os.path
import time

import pytest

from Pages.Employee_Details_page import EmployeeDetailsPage
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
    @pytest.fixture
    def test_Add_Employee(self, Setup, test_Login_ddt):
        self.logger.info("********************** Test_002_Add_Employee  ************************")
        self.logger.info("********************** Verifying Add Employee Test  ************************")
        self.driver = Setup

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
            self.fullname = self.pp.enterfirstname(data[0]) + " " + self.pp.entermiddlename(
                data[1]) + " " + self.pp.enterlastname(data[2])
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
            self.ed = EmployeeDetailsPage(self.driver)
            self.ed.verify_Toast_Message("Success")
            time.sleep(5)
            self.pp.clickEmployeeList()
            time.sleep(5)
            self.pp.enterEmployeename(self.fullname)
            self.pp.clickSearchbutton()

            time.sleep(2)
            self.pp.verifyEmployeenameTable(self.fullname)

        self.logger.info("********************** End of Add Employee Test  ************************")
        self.logger.info("********************** Completed Test_002_Add_Employee ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Personal_Details(self, Setup, test_Add_Employee):
        self.logger.info("********************** Test_003_Add_Employee_Details  ************************")
        self.logger.info("********************** Verifying Add Employee Details Test  ************************")
        self.driver = Setup

        self.pp.clickEmployeeTable()
        time.sleep(5)

        self.ed = EmployeeDetailsPage(self.driver)

        self.rows_add_employee_details = XLUtils.getRowCount(self.path, 'Employee_Personal_Details')
        self.columns_add_employee_details = XLUtils.getColumnCount(self.path, 'Employee_Personal_Details')

        for r in range(2, self.rows_add_employee_details + 1):
            data = []
            for c in range(1, self.columns_add_employee_details + 1):
                cell_data = XLUtils.readData(self.path, 'Employee_Personal_Details', r, c)
                data.append(cell_data)

            processRowData(data)

            self.ed.enter_other_id(data[0])
            self.ed.enter_driving_lic(data[1])
            self.ed.enter_Lic_expiry_date_picker(data[2], data[4], data[5])
            time.sleep(8)
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.ed.select_Nationality_dropdown_values(data[3])
            self.ed.select_Marital_Status_dropdown_values(data[6])
            self.ed.enter_DOB_date_picker(data[7], data[8], data[9])
            time.sleep(8)
            self.driver.execute_script("window.scrollTo(0, -50);")
            self.ed.select_Gender_radio_button(data[10])
            self.ed.click_Personal_details_Save_button()
            self.ed.verify_Toast_Message("Success")
            time.sleep(2)
            self.ed.select_Blood_Type_dropdown_values(data[11])
            self.ed.enter_test_field(data[12])
            self.ed.click_Custom_Fields_Save_button()
            self.ed.verify_Toast_Message("Success")
            time.sleep(3)
            self.ed.click_Custom_Add_Attachment_button()
            self.ed.click_Custom_Browse_Attachment_button()
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

            self.ed.enter_Personal_Details_comment(data[13])
            self.ed.click_Custom_Fields_Attachment_Save_button()
            self.ed.verify_Toast_Message("Success")


        self.logger.info("********************** End of Add Employee Details Test  ************************")
        self.logger.info("********************** Completed Test_003_Add_Employee_Details ************************")
