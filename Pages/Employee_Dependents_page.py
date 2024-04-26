import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementnotfoundException:
    pass


class DependentsPage:
    Dependents_Tile_linkedtext = "Dependents"
    Assigned_Dependents_Add_Button_xpath = ("(//button[@class='oxd-button oxd-button--medium "
                                            "oxd-button--text'])[1]")
    Dependents_Name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Dependents_Relationship_Dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active']"
    Dependents_Relationship_Dropdown_Elements_xpath = "//div[@class='oxd-select-option']"
    Dependents_DOB_Picker_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    Dependents_DOB_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    Dependents_DOB_Month_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Dependents_DOB_Year_xpath = "//li[@class='oxd-calendar-selector-year']"
    Dependents_DOB_Year_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Dependents_DOB_Date_xpath = "//div[@class='oxd-calendar-date']"
    Dependents_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                    "orangehrm-left-space']")
    Dependents_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]"
    Attachment_Add_Button_xpath = "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[2]"
    Attachment_Browse_Button_xpath = "//div[contains(text(),'No file selected')]"
    Attachment_Comment_Area_xpath = "//textarea[@placeholder='Type comment here']"
    Attachment_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                    "orangehrm-left-space']")
    Attachment_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[7]"
    Toast_Message_Xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"

    def __init__(self, driver):
        self.driver = driver

    def click_Dependents_Tile(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Dependents_Tile_linkedtext)))
        element.click()

    def click_Assigned_Dependents_Add_Button(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Assigned_Dependents_Add_Button_xpath)))
        element.click()

    def enter_Dependents_Name(self, dependentsname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Dependents_Name_xpath)))
        element.send_keys(dependentsname)

    def select_Dependents_Relationship_dropdown_values(self, relationship):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Dependents_Relationship_Dropdown_xpath)))
        element.click()
        relationship_dropdown_values = self.driver.find_elements(By.XPATH, self.Dependents_Relationship_Dropdown_Elements_xpath)
        for relation in relationship_dropdown_values:
            if relation.text.strip() == relationship.strip():
                relation.click()
                break

    def enter_Dependents_DOB_picker(self, dobmonth, dobyear, dobdate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        dob_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.Dependents_DOB_Picker_xpath)))
        dob_picker.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        dob_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.Dependents_DOB_Month_xpath)))
        dob_Month.click()
        dob_Month_List = self.driver.find_elements(By.XPATH, self.Dependents_DOB_Month_Lists_xpath)
        for DOB_month in dob_Month_List:
            if DOB_month.text.strip() == dobmonth.strip():
                DOB_month.click()
                break

        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        dob_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.Dependents_DOB_Year_xpath)))
        dob_Year.click()
        dob_Year_List = self.driver.find_elements(By.XPATH, self.Dependents_DOB_Year_Lists_xpath)
        for DOB_year in dob_Year_List:
            try:
                dob_year_value = int(DOB_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if dob_year_value == dobyear:
                assert True
                DOB_year.click()
                break

        time.sleep(3)
        dob_Date_list = self.driver.find_elements(By.XPATH, self.Dependents_DOB_Date_xpath)
        for dob_date in dob_Date_list:
            try:
                dob_date_value = int(dob_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if dob_date_value == dobdate:
                assert True
                dob_date.click()
                break

    def verify_Toast_Message(self, success):
        try:
            toast_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.Toast_Message_Xpath))
            )

            # Once the toast message appears, capture its text
            toast_text = toast_message.text

            if success == toast_text:
                assert True
            else:
                assert False

        except TimeoutException:
            print("Toast message not found within specified timeout period")

    def click_Assigned_Dependents_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Dependents_Save_Button_xpath)))
        element.click()

    def verify_added_Dependent(self, dependentname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Dependents_Row_xpath)))
        Dependent_name = element.text

        if dependentname == Dependent_name:
            assert True
        else:
            assert False

    def click_Dependents_Attachment_Add_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Add_Button_xpath)))
        element.click()

    def click_Dependents_Attachment_Browse_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Browse_Button_xpath)))
        element.click()

    def enter_Dependents_Attachment_Comment(self, comment):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Attachment_Comment_Area_xpath)))
        element.send_keys(comment)

    def click_Dependents_Attachment_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Save_Button_xpath)))
        element.click()

    def verify_Dependent_added_Attachment(self, aatachmentname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Row_xpath)))
        file_name = element.text

        if aatachmentname == file_name:
            assert True
        else:
            assert False