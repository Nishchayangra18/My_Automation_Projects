import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementnotfoundException:
    pass


class EmergencyContactsPage:
    Emergency_Contacts_Tile_linkedtext = "Emergency Contacts"
    Assigned_Emergency_Contact_Add_Button_xpath = ("(//button[@class='oxd-button oxd-button--medium "
                                                   "oxd-button--text'])[1]")
    Emergency_Contact_Name_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Emergency_Contact_Relationship_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    Emergency_Contact_Home_Telephone_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"
    Emergency_Contact_Mobile_xpath = "(//input[@class='oxd-input oxd-input--active'])[5]"
    Emergency_Contact_Work_Telephone_xpath = "(//input[@class='oxd-input oxd-input--active'])[6]"
    Emergency_Contact_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                           "orangehrm-left-space']")
    Emergency_Contact_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]"
    Attachment_Add_Button_xpath = "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[2]"
    Attachment_Browse_Button_xpath = "//div[contains(text(),'No file selected')]"
    Attachment_Comment_Area_xpath = "//textarea[@placeholder='Type comment here']"
    Attachment_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                    "orangehrm-left-space']")
    Attachment_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[9]"
    Toast_Message_Xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"
    Attachment_Edit_Button_xpath = "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def click_Emergency_Contact_Tile(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Emergency_Contacts_Tile_linkedtext)))
        element.click()

    def click_Emergency_Contact_Add_Button(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Assigned_Emergency_Contact_Add_Button_xpath)))
        element.click()

    def enter_Name(self, name):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Name_xpath)))
        element.send_keys(name)

    def enter_Relationship(self, relationship):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Name_xpath)))
        element.send_keys(relationship)

    def enter_Home_Telephone(self, hometelephone):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Relationship_xpath)))
        element.send_keys(hometelephone)

    def enter_Mobile(self, mobile):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Home_Telephone_xpath)))
        element.send_keys(mobile)

    def enter_Work_Telephone(self, worktelephone):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Mobile_xpath)))
        element.send_keys(worktelephone)

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

    def click_Emergency_Contact_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Save_Button_xpath)))
        element.click()

    def verify_added_Emergency_Contact(self, contactname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Emergency_Contact_Row_xpath)))
        file_name = element.text

        if contactname == file_name:
            assert True
        else:
            assert False

    def click_Attachment_Add_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Add_Button_xpath)))
        element.click()

    def click_Attachment_Browse_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Browse_Button_xpath)))
        element.click()

    def enter_Attachment_Comment(self, comment):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Attachment_Comment_Area_xpath)))
        element.send_keys(comment)

    def click_Attachment_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Save_Button_xpath)))
        element.click()

    def verify_added_Attachment(self, aatachmentname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Row_xpath)))
        file_name = element.text

        if aatachmentname == file_name:
            assert True
        else:
            assert False

        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.Attachment_Edit_Button_xpath)))
        edit_button.click()

    def verify_edit_added_Attachment(self, aatachmentname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Row_xpath)))
        file_name = element.text

        if aatachmentname == file_name:
            assert True
        else:
            assert False
