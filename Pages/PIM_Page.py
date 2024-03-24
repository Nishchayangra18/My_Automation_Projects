from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PIMPage:
    Add_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    firstname_textbox_xpath = "//input[@name='firstName']"
    middlename_textbox_xpath = "//input[@name='middleName']"
    lastname_textbox_xpath = "//input[@name='lastName']"
    employee_id_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    create_login_details_slide_button_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    create_login_username_textbox_xpath = "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[6]//input"
    create_login_password_textbox_xpath = "(//div[@class='oxd-input-group oxd-input-field-bottom-space'])[9]//input"
    create_login_confirm_password_textbox_xpath = ("(//div[@class='oxd-input-group oxd-input-field-bottom-space'])["
                                                   "10]//input")
    profile_photo_plus_button_xpath = "//i[@class='oxd-icon bi-plus']"
    save_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    cancel_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    Success_toaster_id = "oxd-toaster_1"
    Sucess_toast_message_xpath = "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"
    Employee_list_xpath = "//a[contains(text(), 'Employee List')]"
    Employee_name_xpath = "(//input[@placeholder='Type for hints...'])[1]"
    Search_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    Table_row_xpath = "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']"
    Table_first_Middle_name_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[3]"
    Table_Last_name_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[4]"

    def __init__(self, driver):
        self.driver = driver

    def clickaddbutton(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Add_button_xpath)))
        element.click()

    def enterfirstname(self, firstname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.firstname_textbox_xpath)))
        element.send_keys(firstname)
        return firstname

    def entermiddlename(self, middlename):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.middlename_textbox_xpath)))
        element.send_keys(middlename)
        return middlename

    def enterlastname(self, lastname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lastname_textbox_xpath)))
        element.send_keys(lastname)
        return lastname

    def enteremployeeid(self, employeeid):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.employee_id_xpath)))
        element.clear()
        element.send_keys(employeeid)

    def clickCreateLoginSlideButton(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.create_login_details_slide_button_xpath)))
        element.click()

    def enterCreateLoginUsername(self, createusername):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.create_login_username_textbox_xpath)))
        element.send_keys(createusername)

    def enterCreateLoginPassword(self, createpassword):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.create_login_password_textbox_xpath)))
        element.send_keys(createpassword)

    def enterCreateLoginConfirmPassword(self, confirmpassword):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.create_login_confirm_password_textbox_xpath)))
        element.send_keys(confirmpassword)

    def addProfilePhoto(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_photo_plus_button_xpath)))
        element.click()

    def clickSavebutton(self):
        element_to_scroll_to = self.driver.find_element(By.XPATH, self.save_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.save_button_xpath)))
        element.click()

    def clickCancelbutton(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancel_button_xpath)))
        element.click()

    def WaitForSuccessToaster(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.Success_toaster_id)))
        print(element.text)

    def GetTextSuccessToastMessage(self, successmessage):
        Success = self.driver.find_element(By.XPATH, self.Sucess_toast_message_xpath).text
        print(Success)

        if successmessage == Success:
            assert True
        else:
            assert False

    def GetTextFullName(self, fullname):
        firstname = self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).text
        lastname = self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).text
        Full_name = firstname + lastname
        print("Full_name: " + Full_name)

        if fullname == Full_name:
            assert True
        else:
            assert False

    def clickEmployeeList(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Employee_list_xpath)))
        element.click()

    def enterEmployeename(self, employeename):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Employee_name_xpath)))
        element.send_keys(employeename)

    def clickSearchbutton(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Search_button_xpath)))
        element.click()

    def verifyEmployeenameTable(self, Employeename):
        Employee_first_name = self.driver.find_element(By.XPATH, self.Table_first_Middle_name_xpath).text
        Employee_last_name = self.driver.find_element(By.XPATH, self.Table_Last_name_xpath).text
        Employee_name = Employee_first_name + " " + Employee_last_name
        print("Employee_name" + Employee_name)

        if Employeename == Employee_name:
            assert True
        else:
            assert False

    def clickEmployeeTable(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Table_first_Middle_name_xpath)))
        element.click()
