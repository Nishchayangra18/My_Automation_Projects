import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementnotfoundException:
    pass


class ImmigrationPage:
    Immigration_Tile_linkedtext = "Immigration"
    Assigned_Immigration_Add_Button_xpath = ("(//button[@class='oxd-button oxd-button--medium "
                                             "oxd-button--text'])[1]")
    Document_Passport_Radio_Button_xpath = "(//div[@class='oxd-radio-wrapper'])[1]"
    Document_Visa_Radio_Button_xpath = "(//div[@class='oxd-radio-wrapper'])[2]"
    Immigration_Number_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Immigration_Issued_Date_Picker_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    Immigration_Issued_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    Immigration_Issued_Month_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Immigration_Issued_Year_xpath = "//li[@class='oxd-calendar-selector-year']"
    Immigration_Issued_Year_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Immigration_Issued_Date_xpath = "//div[@class='oxd-calendar-date']"
    Expiry_Date_Picker_xpath = "(//input[@class='oxd-input oxd-input--active'])[4]"
    Expiry_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    Expiry_Month_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Expiry_Year_xpath = "//li[@class='oxd-calendar-selector-year']"
    Expiry_Year_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Expiry_Date_xpath = "//div[@class='oxd-calendar-date']"
    Eligible_Status_xpath = "(//input[@class='oxd-input oxd-input--active'])[5]"
    Issued_By_Dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active']"
    Issued_By_Dropdown_Lists_xpath = "//div[@class='oxd-select-option']"
    Eligible_Review_Date_Picker_xpath = "(//input[@class='oxd-input oxd-input--active'])[6]"
    Eligible_Review_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    Eligible_Review_Month_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Eligible_Review_Year_xpath = "//li[@class='oxd-calendar-selector-year']"
    Eligible_Review_Year_Lists_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Eligible_Review_Date_xpath = "//div[@class='oxd-calendar-date']"
    Immigration_Comment_Area_xpath = "//textarea[@placeholder='Type Comments here']"
    Immigration_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                     "orangehrm-left-space']")
    Immigration_Document_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]"
    Immigration_Number_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[3]"
    Attachment_Add_Button_xpath = "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[2]"
    Attachment_Browse_Button_xpath = "//div[contains(text(),'No file selected')]"
    Attachment_Comment_Area_xpath = "//textarea[@placeholder='Type comment here']"
    Attachment_Save_Button_xpath = ("//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                    "orangehrm-left-space']")
    Attachment_Row_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[9]"
    Toast_Message_Xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"

    def __init__(self, driver):
        self.driver = driver

    def click_Immigration_Tile(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Immigration_Tile_linkedtext)))
        element.click()

    def click_Assigned_Immigration_Add_Button(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Assigned_Immigration_Add_Button_xpath)))
        element.click()

    def select_Document_Radio_Button(self, document):
        if document == "Passport":
            wait = WebDriverWait(self.driver, 20)  # set a max wait time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Document_Passport_Radio_Button_xpath)))
            element.click()
        elif document == "Visa":
            wait = WebDriverWait(self.driver, 20)  # set a max wait time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Document_Visa_Radio_Button_xpath)))
            element.click()
        else:
            wait = WebDriverWait(self.driver, 20)  # set a max wait time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Document_Passport_Radio_Button_xpath)))
            if element.is_selected():
                assert True
            else:
                assert False

    def enter_Number(self, number):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Immigration_Number_xpath)))
        element.send_keys(number)

    def select_Immigration_Issued_By_dropdown_values(self, issuedby):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Issued_By_Dropdown_xpath)))
        element.click()
        Immigration_Issued_By_dropdown_values = self.driver.find_elements(By.XPATH,
                                                                          self.Issued_By_Dropdown_Lists_xpath)
        for issued_by in Immigration_Issued_By_dropdown_values:
            if issued_by.text.strip() == issuedby.strip():
                issued_by.click()
                break

    def enter_Immigration_Issued_Date_picker(self, issuedmonth, issuedyear, issueddate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Issued_Date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.Immigration_Number_xpath)))
        Immigration_Issued_Date_picker.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Issued_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.Immigration_Issued_Month_xpath)))
        Immigration_Issued_Month.click()
        Immigration_Issued_Month_List = self.driver.find_elements(By.XPATH, self.Immigration_Issued_Month_Lists_xpath)
        for Immigration_Issued_month in Immigration_Issued_Month_List:
            if Immigration_Issued_month.text.strip() == issuedmonth.strip():
                Immigration_Issued_month.click()
                break

        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Issued_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.Immigration_Issued_Year_xpath)))
        Immigration_Issued_Year.click()
        Immigration_Issued_Year_List = self.driver.find_elements(By.XPATH, self.Immigration_Issued_Year_Lists_xpath)
        for Immigration_Issued_year in Immigration_Issued_Year_List:
            try:
                Immigration_Issued_year_value = int(Immigration_Issued_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Immigration_Issued_year_value == issuedyear:
                assert True
                Immigration_Issued_year.click()
                break

        time.sleep(3)
        Immigration_Issued_Date_list = self.driver.find_elements(By.XPATH, self.Immigration_Issued_Date_xpath)
        for Immigration_Issued_date in Immigration_Issued_Date_list:
            try:
                Immigration_Issued_date_value = int(Immigration_Issued_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Immigration_Issued_date_value == issueddate:
                assert True
                Immigration_Issued_date.click()
                break

    def enter_Immigration_Expiry_Date_picker(self, expirymonth, expiryyear, expirydate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Expiry_Date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.Immigration_Issued_Date_Picker_xpath)))
        Immigration_Expiry_Date_picker.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Expiry_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.Expiry_Month_xpath)))
        Immigration_Expiry_Month.click()
        Immigration_Expiry_Month_List = self.driver.find_elements(By.XPATH, self.Expiry_Month_Lists_xpath)
        for Immigration_Expiry_month in Immigration_Expiry_Month_List:
            if Immigration_Expiry_month.text.strip() == expirymonth.strip():
                Immigration_Expiry_month.click()
                break

        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigration_Expiry_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.Expiry_Year_xpath)))
        Immigration_Expiry_Year.click()
        Immigration_Expiry_Year_List = self.driver.find_elements(By.XPATH, self.Expiry_Year_Lists_xpath)
        for Immigration_Expiry_year in Immigration_Expiry_Year_List:
            try:
                Immigration_Expiry_year_value = int(Immigration_Expiry_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Immigration_Expiry_year_value == expiryyear:
                assert True
                Immigration_Expiry_year.click()
                break

        time.sleep(3)
        Immigration_Expiry_Date_list = self.driver.find_elements(By.XPATH, self.Expiry_Date_xpath)
        for Immigration_Expiry_date in Immigration_Expiry_Date_list:
            try:
                Immigration_Expiry_date_value = int(Immigration_Expiry_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Immigration_Expiry_date_value == expirydate:
                assert True
                Immigration_Expiry_date.click()
                break

    def enter_Eligible_Status(self, eligiblestatus):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Expiry_Date_Picker_xpath)))
        element.send_keys(eligiblestatus)

    def enter_Eligible_Review_Date_picker(self, reviewmonth, reviewyear, reviewdate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Eligible_Review_Date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.Eligible_Review_Date_Picker_xpath)))
        Eligible_Review_Date_picker.click()
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Eligible_Review_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.Eligible_Review_Month_xpath)))
        Eligible_Review_Month.click()
        Eligible_Review_Month_List = self.driver.find_elements(By.XPATH, self.Eligible_Review_Month_Lists_xpath)
        for Eligible_Review_month in Eligible_Review_Month_List:
            if Eligible_Review_month.text.strip() == reviewmonth.strip():
                Eligible_Review_month.click()
                break


        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Eligible_Review_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.Eligible_Review_Year_xpath)))
        Eligible_Review_Year.click()
        Eligible_Review_Year_List = self.driver.find_elements(By.XPATH, self.Eligible_Review_Year_Lists_xpath)
        for Eligible_Review_year in Eligible_Review_Year_List:
            try:
                Eligible_Review_year_value = int(Eligible_Review_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Eligible_Review_year_value == reviewyear:
                assert True
                Eligible_Review_year.click()
                break


        time.sleep(3)
        Eligible_Review_Date_list = self.driver.find_elements(By.XPATH, self.Eligible_Review_Date_xpath)
        for Eligible_Review_date in Eligible_Review_Date_list:
            try:
                Eligible_Review_date_value = int(Eligible_Review_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if Eligible_Review_date_value == reviewdate:
                assert True
                Eligible_Review_date.click()
                break

    def enter_Immigration_Comments(self, immigrationcomments):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Immigration_Comment_Area_xpath)))
        element.send_keys(immigrationcomments)

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

    def click_Assigned_Immigration_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Immigration_Save_Button_xpath)))
        element.click()

    def verify_added_Immigrant(self, immigrantdocument, immigrantnumber):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Immigration_Document_Row_xpath)))
        Immigrant_document = element.text.strip()
        print(Immigrant_document)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Immigrant_Number = wait.until(EC.element_to_be_clickable((By.XPATH, self.Immigration_Number_Row_xpath)))
        Immigrant_number_Value = int(Immigrant_Number.text)
        print(Immigrant_number_Value)

        if immigrantdocument == Immigrant_document and immigrantnumber == Immigrant_number_Value:
            assert True
        else:
            assert False

    def click_Immigration_Attachment_Add_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Add_Button_xpath)))
        element.click()

    def click_Immigration_Attachment_Browse_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Browse_Button_xpath)))
        element.click()

    def enter_Immigration_Attachment_Comment(self, comment):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Attachment_Comment_Area_xpath)))
        element.send_keys(comment)

    def click_Immigration_Attachment_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Save_Button_xpath)))
        element.click()

    def verify_Immigration_added_Attachment(self, aatachmentname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Attachment_Row_xpath)))
        file_name = element.text

        if aatachmentname == file_name:
            assert True
        else:
            assert False
