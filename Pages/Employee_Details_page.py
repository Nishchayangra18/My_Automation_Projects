import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EmployeeDetailsPage:
    Other_id__xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    Driving_Lic_textbox_xpath = "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[6]//input"
    Lic_Expiry_Date_picker_xpath = "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]"
    Lic_Expiry_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    Lic_Expiry_Month_List_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Lic_Expiry_Year_xpath = "//div[@class='oxd-calendar-selector-year-selected']"
    Lic_Expiry_Year_List_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    Lic_Expiry_Date_xpath = "//div[@class='oxd-calendar-date']"
    Nationality_dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    Nationality_dropdown_elements_xpath = "//div[@class='oxd-select-option']"
    Marital_Status_Dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    Marital_Status_Dropdown_elements_xpath = "//div[@class='oxd-select-option']"
    DOB_Picker_xpath = "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]"
    DOB_Month_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    DOB_Month_List_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    DOB_Year_xpath = "//div[@class='oxd-calendar-selector-year-selected']"
    DOB_Year_List_xpath = "//li[@class='oxd-calendar-dropdown--option']"
    DOB_Date_xpath = "//div[@class='oxd-calendar-date']"
    Male_Radio_button_xpath = ("(//span[@class='oxd-radio-input oxd-radio-input--active --label-right "
                               "oxd-radio-input'])[1]")
    Female_Radio_button_xpath = ("(//span[@class='oxd-radio-input oxd-radio-input--active --label-right "
                                 "oxd-radio-input'])[2]")
    Personal_Details_Save_button_xpath = ("(//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                          "orangehrm-left-space'])[1]")
    Blood_Type_Dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[3]"
    Blood_Type_Dropdown_List_xpath = "//div[@class='oxd-select-option']"
    Test_field_Textbox_xpath = "(//input[@class='oxd-input oxd-input--active'])[7]"
    Custom_Fields_Save_button_xpath = ("(//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
                                       "orangehrm-left-space'])[2]")

    def __init__(self, driver):
        self.driver = driver

    def enter_other_id(self, otherid):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Other_id__xpath)))
        element.send_keys(otherid)

    def enter_driving_lic(self, drivinglicence):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Driving_Lic_textbox_xpath)))
        element.send_keys(drivinglicence)

    def enter_Lic_expiry_date_picker(self, licexpmonth, licexpyear, licexpdate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Lic_date_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.Lic_Expiry_Date_picker_xpath)))
        Lic_date_picker.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Lic_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.Lic_Expiry_Month_xpath)))
        Lic_Month.click()
        Lic_Month_List = self.driver.find_elements(By.XPATH, self.Lic_Expiry_Month_List_xpath)
        for lic_month in Lic_Month_List:
            if lic_month.text.strip() == licexpmonth.strip():
                lic_month.click()
                break

        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        Lic_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.Lic_Expiry_Year_xpath)))
        Lic_Year.click()
        Lic_Year_List = self.driver.find_elements(By.XPATH, self.Lic_Expiry_Year_List_xpath)
        for lic_year in Lic_Year_List:
            try:
                lic_year_value = int(lic_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if lic_year_value == licexpyear:
                assert True
                lic_year.click()
                break

        time.sleep(3)
        Lic_Date_list = self.driver.find_elements(By.XPATH, self.Lic_Expiry_Date_xpath)
        for lic_date in Lic_Date_list:
            try:
                lic_date_value = int(lic_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if lic_date_value == licexpdate:
                assert True
                lic_date.click()
                break

    def select_Nationality_dropdown_values(self, nationality):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Nationality_dropdown_xpath)))
        element.click()
        nationality_dropdown_values = self.driver.find_elements(By.XPATH, self.Nationality_dropdown_elements_xpath)
        for nations in nationality_dropdown_values:
            if nations.text.strip() == nationality.strip():
                nations.click()
                break

    def select_Marital_Status_dropdown_values(self, maritalstatus):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Marital_Status_Dropdown_xpath)))
        element.click()
        marital_Status_dropdown_values = self.driver.find_elements(By.XPATH,
                                                                   self.Marital_Status_Dropdown_elements_xpath)
        for marital_status in marital_Status_dropdown_values:
            if marital_status.text.strip() == maritalstatus.strip():
                marital_status.click()
                break

    def enter_DOB_date_picker(self, dobmonth, dobyear, dobdate):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        DOB_picker = wait.until(EC.visibility_of_element_located((By.XPATH, self.DOB_Picker_xpath)))
        DOB_picker.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        DOB_Month = wait.until(EC.visibility_of_element_located((By.XPATH, self.DOB_Month_xpath)))
        DOB_Month.click()
        DOB_Month_List = self.driver.find_elements(By.XPATH, self.DOB_Month_List_xpath)
        for dob_month in DOB_Month_List:
            if dob_month.text.strip() == dobmonth.strip():
                dob_month.click()
                break

        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        DOB_Year = wait.until(EC.visibility_of_element_located((By.XPATH, self.DOB_Year_xpath)))
        DOB_Year.click()
        DOB_Year_List = self.driver.find_elements(By.XPATH, self.DOB_Year_List_xpath)
        for dob_year in DOB_Year_List:
            try:
                dob_year_value = int(dob_year.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if dob_year_value == dobyear:
                assert True
                dob_year.click()
                break

        time.sleep(3)
        DOB_Date_list = self.driver.find_elements(By.XPATH, self.DOB_Date_xpath)
        for dob_date in DOB_Date_list:
            try:
                dob_date_value = int(dob_date.text)
            except ValueError:
                continue  # Skip this element if it's not a valid integer
            if dob_date_value == dobdate:
                assert True
                dob_date.click()
                break

    def select_Gender_radio_button(self, gender):
        if gender == "Male":
            wait = WebDriverWait(self.driver, 20)  # set a max wait time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Male_Radio_button_xpath)))
            element.click()
        elif gender == "Female":
            wait = WebDriverWait(self.driver, 20)  # set a max wait time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Female_Radio_button_xpath)))
            element.click()

    def click_Personal_details_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Personal_Details_Save_button_xpath)))
        element.click()

    def select_Blood_Type_dropdown_values(self, bloodtype):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Blood_Type_Dropdown_xpath)))
        element.click()
        bloodtype_dropdown_values = self.driver.find_elements(By.XPATH, self.Blood_Type_Dropdown_List_xpath)
        for blood_type in bloodtype_dropdown_values:
            if blood_type.text.strip() == bloodtype.strip():
                blood_type.click()
                break

    def enter_test_field(self, testfield):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Test_field_Textbox_xpath)))
        element.send_keys(testfield)

    def click_Custom_Fields_Save_button(self):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Custom_Fields_Save_button_xpath)))
        element.click()
