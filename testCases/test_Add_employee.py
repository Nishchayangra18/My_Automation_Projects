import os.path
import time

import pytest
from selenium import webdriver

from Pages.Employee_Personal_Details_page import EmployeeDetailsPage
from Pages.Login_Page import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
from Pages.Dashboard_Page import DashboardPage
from Pages.PIM_Page import PIMPage
from pynput.keyboard import Key, Controller
from Pages.Employee_Contact_Details_page import EmployeeContactDetailsPage
from Pages.Employee_Emergency_Contacts_page import EmergencyContactsPage


def processRowData(data):
    print("Processing Row Data:")
    for index, value in enumerate(data):
        print(f"Column {index + 1}: {value}")


class Test_002_Add_Employee:
    path = ".//testData/OrangeHRM_Testdata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.fixture(scope="function")
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

    @pytest.fixture(scope="function")
    def test_Personal_Details_Fixture(self, Setup, test_Add_Employee):
        self.logger.info("********************** Verifying test_Personal_Details Test  ************************")
        self.driver = Setup
        # self.pp = PIMPage(self.driver)

        self.pp.clickEmployeeTable()
        time.sleep(5)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Personal_Details(self, Setup, test_Personal_Details_Fixture):
        self.ed = EmployeeDetailsPage(self.driver)

        self.rows_Personal_employee_details = XLUtils.getRowCount(self.path, 'Employee_Personal_Details')
        self.columns_Personal_employee_details = XLUtils.getColumnCount(self.path, 'Employee_Personal_Details')

        for r in range(2, self.rows_Personal_employee_details + 1):
            data = []
            for c in range(1, self.columns_Personal_employee_details + 1):
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
            time.sleep(3)
            self.ed.verify_added_custom_field_Attachment(self.dp_jpg_name)

        self.logger.info("********************** End of test_Personal_Details Test ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Contact_Details(self, Setup, test_Login_ddt):
        self.logger.info("********************** Verifying test_Contact_Details Test  ************************")
        self.driver = Setup
        self.ecd = EmployeeContactDetailsPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 0);")

        self.ecd.click_Contact_Details_Tile()
        self.driver.execute_script("window.scrollTo(0, 0);")

        self.rows_employee_Contact_details = XLUtils.getRowCount(self.path, 'Employee_Contact_Details')
        self.columns_employee_Contact_details = XLUtils.getColumnCount(self.path, 'Employee_Contact_Details')

        for r in range(2, self.rows_employee_Contact_details + 1):
            data = []
            for c in range(1, self.columns_employee_Contact_details + 1):
                cell_data = XLUtils.readData(self.path, 'Employee_Contact_Details', r, c)
                data.append(cell_data)

            processRowData(data)

            time.sleep(5)
            self.ecd.enter_Street1(data[0])
            time.sleep(2)
            self.ecd.enter_Street2(data[1])
            self.ecd.enter_City(data[2])
            self.ecd.enter_State(data[3])
            self.ecd.enter_ZIP(data[4])
            self.ecd.select_Country_dropdown_values(data[5])
            self.ecd.enter_Telephone_Home(data[6])
            time.sleep(2)
            self.ecd.enter_Telephone_Mobile(data[7])
            self.ecd.enter_Telephone_Work(data[8])
            self.ecd.enter_Work_Email(data[9])
            self.ecd.enter_Other_Email(data[10])
            self.ecd.click_Contact_Details_Save_button()
            time.sleep(3)
            self.ecd.verify_Toast_Message("Success")
            time.sleep(2)
            self.ecd.click_Attachment_Add_button()
            self.ecd.click_Attachment_Browse_button()
            self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
            self.slash = "\\"
            self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
            self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
            time.sleep(5)
            try:
                keyword = Controller()
                keyword.type(self.dp_jpg_path)
                keyword.press(Key.enter)
                keyword.release(Key.enter)
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
            self.ecd.enter_Attachment_Comment(data[11])
            self.ecd.click_Attachment_Save_button()
            self.ecd.verify_Toast_Message("Success")
            time.sleep(3)

            self.ecd.verify_added_Attachment(self.dp_jpg_name, "No Records Found")

        self.logger.info("********************** End of test_Contact_Details Test ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Emergency_Contact(self, Setup, test_Login_ddt):
        self.logger.info("********************** Verifying test_Emergency_Contact Test  ************************")
        self.driver = Setup
        self.emergency_contact = EmergencyContactsPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 0);")

        self.emergency_contact.click_Emergency_Contact_Tile()
        self.emergency_contact.click_Emergency_Contact_Add_Button()

        self.rows_emergency_Contacts = XLUtils.getRowCount(self.path, 'Emergency_Contacts')
        self.columns_emergency_Contacts = XLUtils.getColumnCount(self.path, 'Emergency_Contacts')

        for r in range(2, self.rows_emergency_Contacts + 1):
            data = []
            for c in range(1, self.columns_emergency_Contacts + 1):
                cell_data = XLUtils.readData(self.path, 'Emergency_Contacts', r, c)
                data.append(cell_data)

            processRowData(data)

            self.emergency_contact.enter_Name(data[0])
            self.emergency_contact.enter_Relationship(data[1])
            self.emergency_contact.enter_Home_Telephone(data[2])
            self.emergency_contact.enter_Mobile(data[3])
            self.emergency_contact.enter_Work_Telephone(data[4])
            self.emergency_contact.click_Emergency_Contact_Save_button()
            self.emergency_contact.verify_added_Emergency_Contact(data[0])
            time.sleep(3)
            self.emergency_contact.verify_Toast_Message("Success")
            time.sleep(2)
            self.emergency_contact.click_Attachment_Add_button()
            self.emergency_contact.click_Attachment_Browse_button()
            self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
            self.slash = "\\"
            self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
            self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
            time.sleep(5)
            try:
                keyword = Controller()
                keyword.type(self.dp_jpg_path)
                keyword.press(Key.enter)
                keyword.release(Key.enter)
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
            self.emergency_contact.enter_Attachment_Comment(data[5])
            self.emergency_contact.click_Attachment_Save_button()
            self.emergency_contact.verify_Toast_Message("Success")
            time.sleep(3)

            self.emergency_contact.verify_added_Attachment(self.dp_jpg_name)
            time.sleep(3)

            self.emergency_contact.click_Attachment_Browse_button()
            self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_Edit_Dp_Upload.jpg"))
            self.slash = "\\"
            self.edit_dp_jpg_name = os.path.basename("testData/Test_Edit_Dp_Upload.jpg")
            self.edit_dp_jpg_path = self.Directory_path + self.slash + self.edit_dp_jpg_name
            time.sleep(5)
            try:
                keyword = Controller()
                keyword.type(self.edit_dp_jpg_path)
                keyword.press(Key.enter)
                keyword.release(Key.enter)
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
            self.emergency_contact.enter_Attachment_Comment(data[6])
            self.emergency_contact.click_Attachment_Save_button()
            self.emergency_contact.verify_Toast_Message("Success")
            time.sleep(3)

            self.emergency_contact.verify_edit_added_Attachment(self.edit_dp_jpg_name)

        self.logger.info("********************** End of test_Emergency_Contact Test ************************")

