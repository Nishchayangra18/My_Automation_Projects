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
from Pages.Employee_Dependents_page import DependentsPage
from Pages.Employee_Immigration_page import ImmigrationPage


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
    #
    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_Contact_Details(self, Setup, test_Login_ddt):
    #     self.logger.info("********************** Verifying test_Contact_Details Test  ************************")
    #     self.driver = Setup
    #     self.ecd = EmployeeContactDetailsPage(self.driver)
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #
    #     self.ecd.click_Contact_Details_Tile()
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #
    #     self.rows_employee_Contact_details = XLUtils.getRowCount(self.path, 'Employee_Contact_Details')
    #     self.columns_employee_Contact_details = XLUtils.getColumnCount(self.path, 'Employee_Contact_Details')
    #
    #     for r in range(2, self.rows_employee_Contact_details + 1):
    #         data = []
    #         for c in range(1, self.columns_employee_Contact_details + 1):
    #             cell_data = XLUtils.readData(self.path, 'Employee_Contact_Details', r, c)
    #             data.append(cell_data)
    #
    #         processRowData(data)
    #
    #         time.sleep(5)
    #         self.ecd.enter_Street1(data[0])
    #         time.sleep(2)
    #         self.ecd.enter_Street2(data[1])
    #         self.ecd.enter_City(data[2])
    #         self.ecd.enter_State(data[3])
    #         self.ecd.enter_ZIP(data[4])
    #         self.ecd.select_Country_dropdown_values(data[5])
    #         self.ecd.enter_Telephone_Home(data[6])
    #         time.sleep(2)
    #         self.ecd.enter_Telephone_Mobile(data[7])
    #         self.ecd.enter_Telephone_Work(data[8])
    #         self.ecd.enter_Work_Email(data[9])
    #         self.ecd.enter_Other_Email(data[10])
    #         self.ecd.click_Contact_Details_Save_button()
    #         time.sleep(3)
    #         self.ecd.verify_Toast_Message("Success")
    #         time.sleep(2)
    #         self.ecd.click_Attachment_Add_button()
    #         self.ecd.click_Attachment_Browse_button()
    #         self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
    #         self.slash = "\\"
    #         self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
    #         self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
    #         time.sleep(5)
    #         try:
    #             keyword = Controller()
    #             keyword.type(self.dp_jpg_path)
    #             keyword.press(Key.enter)
    #             keyword.release(Key.enter)
    #             time.sleep(5)
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #         self.ecd.enter_Attachment_Comment(data[11])
    #         self.ecd.click_Attachment_Save_button()
    #         self.ecd.verify_Toast_Message("Success")
    #         time.sleep(3)
    #
    #         self.ecd.verify_added_Attachment(self.dp_jpg_name, "No Records Found")
    #
    #     self.logger.info("********************** End of test_Contact_Details Test ************************")
    #
    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_Emergency_Contact(self, Setup, test_Login_ddt):
    #     self.logger.info("********************** Verifying test_Emergency_Contact Test  ************************")
    #     self.driver = Setup
    #     self.emergency_contact = EmergencyContactsPage(self.driver)
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #
    #     self.emergency_contact.click_Emergency_Contact_Tile()
    #     self.emergency_contact.click_Emergency_Contact_Add_Button()
    #
    #     self.rows_emergency_Contacts = XLUtils.getRowCount(self.path, 'Emergency_Contacts')
    #     self.columns_emergency_Contacts = XLUtils.getColumnCount(self.path, 'Emergency_Contacts')
    #
    #     for r in range(2, self.rows_emergency_Contacts + 1):
    #         data = []
    #         for c in range(1, self.columns_emergency_Contacts + 1):
    #             cell_data = XLUtils.readData(self.path, 'Emergency_Contacts', r, c)
    #             data.append(cell_data)
    #
    #         processRowData(data)
    #
    #         self.emergency_contact.enter_Name(data[0])
    #         self.emergency_contact.enter_Relationship(data[1])
    #         self.emergency_contact.enter_Home_Telephone(data[2])
    #         self.emergency_contact.enter_Mobile(data[3])
    #         self.emergency_contact.enter_Work_Telephone(data[4])
    #         self.emergency_contact.click_Emergency_Contact_Save_button()
    #         self.emergency_contact.verify_added_Emergency_Contact(data[0])
    #         time.sleep(3)
    #         self.emergency_contact.verify_Toast_Message("Success")
    #         time.sleep(2)
    #         self.emergency_contact.click_Attachment_Add_button()
    #         self.emergency_contact.click_Attachment_Browse_button()
    #         self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
    #         self.slash = "\\"
    #         self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
    #         self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
    #         time.sleep(5)
    #         try:
    #             keyword = Controller()
    #             keyword.type(self.dp_jpg_path)
    #             keyword.press(Key.enter)
    #             keyword.release(Key.enter)
    #             time.sleep(5)
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #         self.emergency_contact.enter_Attachment_Comment(data[5])
    #         self.emergency_contact.click_Attachment_Save_button()
    #         self.emergency_contact.verify_Toast_Message("Success")
    #         time.sleep(3)
    #
    #         self.emergency_contact.verify_added_Attachment(self.dp_jpg_name)
    #         time.sleep(3)
    #
    #         self.emergency_contact.click_Attachment_Browse_button()
    #         self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_Edit_Dp_Upload.jpg"))
    #         self.slash = "\\"
    #         self.edit_dp_jpg_name = os.path.basename("testData/Test_Edit_Dp_Upload.jpg")
    #         self.edit_dp_jpg_path = self.Directory_path + self.slash + self.edit_dp_jpg_name
    #         time.sleep(5)
    #         try:
    #             keyword = Controller()
    #             keyword.type(self.edit_dp_jpg_path)
    #             keyword.press(Key.enter)
    #             keyword.release(Key.enter)
    #             time.sleep(5)
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #         self.emergency_contact.enter_Attachment_Comment(data[6])
    #         self.emergency_contact.click_Attachment_Save_button()
    #         self.emergency_contact.verify_Toast_Message("Success")
    #         time.sleep(3)
    #
    #         self.emergency_contact.verify_edit_added_Attachment(self.edit_dp_jpg_name)
    #
    #     self.logger.info("********************** End of test_Emergency_Contact Test ************************")
    #
    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_Dependents(self, Setup, test_Login_ddt):
    #     self.logger.info("********************** Verifying test_Dependents Test  ************************")
    #     self.driver = Setup
    #     self.dependents = DependentsPage(self.driver)
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #
    #     self.dependents.click_Dependents_Tile()
    #     self.dependents.click_Assigned_Dependents_Add_Button()
    #
    #     self.rows_Dependents = XLUtils.getRowCount(self.path, 'Dependents')
    #     self.columns_Dependents = XLUtils.getColumnCount(self.path, 'Dependents')
    #
    #     for r in range(2, self.rows_Dependents + 1):
    #         data = []
    #         for c in range(1, self.columns_Dependents + 1):
    #             cell_data = XLUtils.readData(self.path, 'Dependents', r, c)
    #             data.append(cell_data)
    #
    #         processRowData(data)
    #
    #         self.dependents.enter_Dependents_Name(data[0])
    #         self.dependents.select_Dependents_Relationship_dropdown_values(data[1])
    #         self.dependents.enter_Dependents_DOB_picker(data[2], data[3], data[4])
    #         self.driver.execute_script("window.scrollTo(0, 0);")
    #         self.dependents.click_Assigned_Dependents_Save_button()
    #         time.sleep(3)
    #         self.dependents.verify_Toast_Message("Success")
    #         self.dependents.verify_added_Dependent(data[0])
    #         time.sleep(2)
    #         self.dependents.click_Dependents_Attachment_Add_button()
    #         self.dependents.click_Dependents_Attachment_Browse_button()
    #         self.Directory_path = os.path.dirname(os.path.realpath(".//testData/Test_dp_upload.jpg"))
    #         self.slash = "\\"
    #         self.dp_jpg_name = os.path.basename("testData/Test_dp_upload.jpg")
    #         self.dp_jpg_path = self.Directory_path + self.slash + self.dp_jpg_name
    #         time.sleep(5)
    #         try:
    #             keyword = Controller()
    #             keyword.type(self.dp_jpg_path)
    #             keyword.press(Key.enter)
    #             keyword.release(Key.enter)
    #             time.sleep(5)
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #         self.dependents.enter_Dependents_Attachment_Comment(data[5])
    #         self.dependents.click_Dependents_Attachment_Save_button()
    #         self.dependents.verify_Toast_Message("Success")
    #         time.sleep(3)
    #
    #         self.dependents.verify_Dependent_added_Attachment(self.dp_jpg_name)
    #
    #     self.logger.info("********************** End of test_Dependents Test ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Immigration(self, Setup, test_Login_ddt):
        self.logger.info("********************** Verifying test_Immigration Test  ************************")
        self.driver = Setup
        self.immigration = ImmigrationPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 0);")

        self.immigration.click_Immigration_Tile()
        self.immigration.click_Assigned_Immigration_Add_Button()

        self.rows_Immigration = XLUtils.getRowCount(self.path, 'Immigration')
        self.columns_Immigration = XLUtils.getColumnCount(self.path, 'Immigration')

        for r in range(2, self.rows_Immigration + 1):
            data = []
            for c in range(1, self.columns_Immigration + 1):
                cell_data = XLUtils.readData(self.path, 'Immigration', r, c)
                data.append(cell_data)

            processRowData(data)

            self.immigration.select_Document_Radio_Button(data[0])
            self.immigration.enter_Number(data[1])
            self.immigration.enter_Immigration_Issued_Date_picker(data[3], data[4], data[5])
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.immigration.enter_Immigration_Expiry_Date_picker(data[6], data[7], data[8])
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.immigration.enter_Eligible_Status(data[9])
            self.immigration.select_Immigration_Issued_By_dropdown_values(data[2])
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.immigration.enter_Eligible_Review_Date_picker(data[10], data[11], data[12])
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.immigration.enter_Immigration_Comments(data[13])
            self.immigration.click_Assigned_Immigration_Save_button()
            time.sleep(3)
            self.immigration.verify_Toast_Message("Success")
            self.immigration.verify_added_Immigrant(data[0], data[1])
            time.sleep(2)
            self.immigration.click_Immigration_Attachment_Add_button()
            self.immigration.click_Immigration_Attachment_Browse_button()
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
            self.immigration.enter_Immigration_Attachment_Comment(data[14])
            self.immigration.click_Immigration_Attachment_Save_button()
            self.immigration.verify_Toast_Message("Success")
            time.sleep(3)

            self.immigration.verify_Immigration_added_Attachment(self.dp_jpg_name)

        self.logger.info("********************** End of test_Immigration Test ************************")