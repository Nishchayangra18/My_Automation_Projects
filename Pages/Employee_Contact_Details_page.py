import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementnotfoundException:
    pass


class EmployeeContactDetailsPage:
    Contact_Details_Tile_linkedtext = "Contact Details"
    Street1_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Street2_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    City_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"
    State_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[5]"
    ZIP_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[6]"
    Country_Dropdown_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    Country_dropdown_elements_xpath = "//div[@class='oxd-select-option']"
    Telephone_Home_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[7]"
    Telephone_Mobile_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[8]"
    Telephone_Work_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[9]"
    Work_Email_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[10]"
    Other_Email_textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[11]"
    Contact_Details_Save_button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                         "orangehrm-left-space']")
    Attachment_Add_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--text']"
    Browse_Attachment_xpath = "//i[@class='oxd-icon bi-upload oxd-file-input-icon']"
    Attachment_Comment_area_xpath = "//textarea[@placeholder='Type comment here']"
    Attachment_Save_button_xpath = ("(//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                    "orangehrm-left-space'])[2]")
    Toast_Message_Xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"

    Attachment_row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]"
    Attachment_delete_button_xpath = "//button[@class='oxd-icon-button oxd-table-cell-action-space'][2]"
    Attachment_Delete_Confirmation_Yes_button_xpath = ("//button[@class='oxd-button oxd-button--medium "
                                                       "oxd-button--label-danger orangehrm-button-margin']")
    No_Attachment_xpath = "//span[@class='oxd-text oxd-text--span']"

    def __init__(self, driver):
        self.driver = driver

    def click_Contact_Details_Tile(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Contact_Details_Tile_linkedtext)))
        element.click()

    def enter_Street1(self, street1):
        # wait = WebDriverWait(self.driver, 20)  # set a max wait time
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Street1_textbox_xpath)))
        # element.send_keys(street1)
        self.driver.find_element(By.XPATH, self.Street1_textbox_xpath).send_keys(street1)

    def enter_Street2(self, street2):
        # try:
        #     wait = WebDriverWait(self.driver, 20)  # set a max wait time
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Street2_textbox_xpath)))
        #     element.send_keys(street2)
        # except ElementnotfoundException:
        #     assert False
        self.driver.find_element(By.XPATH, self.Street1_textbox_xpath).send_keys(street2)

    def enter_City(self, city):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Street2_textbox_xpath)))
        element.send_keys(city)

    def enter_State(self, state):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.City_textbox_xpath)))
        element.send_keys(state)

    def enter_ZIP(self, zip):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.State_textbox_xpath)))
        element.send_keys(zip)

    def select_Country_dropdown_values(self, country):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Country_Dropdown_xpath)))
        element.click()
        country_dropdown_values = self.driver.find_elements(By.XPATH, self.Country_dropdown_elements_xpath)
        for countries in country_dropdown_values:
            if countries.text.strip() == country.strip():
                countries.click()
                break

    def enter_Telephone_Home(self, telephonehome):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Telephone_Home_textbox_xpath)))
        element.send_keys(telephonehome)

    def enter_Telephone_Mobile(self, telephonemobile):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Telephone_Home_textbox_xpath)))
        element.send_keys(telephonemobile)

    def enter_Telephone_Work(self, telephonework):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Telephone_Mobile_textbox_xpath)))
        element.send_keys(telephonework)

    def enter_Work_Email(self, workemail):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Work_Email_textbox_xpath)))
        element.send_keys(workemail)

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

    def enter_Other_Email(self, otheremail):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Work_Email_textbox_xpath)))
        element.send_keys(otheremail)

    def click_Contact_Details_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Contact_Details_Save_button_xpath)))
        element.click()

    def click_Attachment_Add_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Add_button_xpath)))
        element.click()

    def click_Attachment_Browse_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Browse_Attachment_xpath)))
        element.click()

    def enter_Attachment_Comment(self, comment):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Attachment_Comment_area_xpath)))
        element.send_keys(comment)

    def click_Attachment_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Save_button_xpath)))
        element.click()

    def verify_added_Attachment(self, aatachmentname, norecordfound):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_row_xpath)))
        file_name = element.text

        if aatachmentname == file_name:
            assert True
        else:
            assert False

        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        delete_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.Attachment_delete_button_xpath)))
        delete_button.click()

        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        delete_Yes_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.Attachment_Delete_Confirmation_Yes_button_xpath)))
        delete_Yes_button.click()

        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        No_Record = wait.until(EC.visibility_of_element_located((By.XPATH, self.No_Attachment_xpath)))
        No_Attachment_Found = No_Record.text
        if No_Attachment_Found == norecordfound:
            assert True
        else:
            assert False

