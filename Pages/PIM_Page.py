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

    def entermiddlename(self, middlename):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.middlename_textbox_xpath)))
        element.send_keys(middlename)

    def enterlastname(self, lastname):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lastname_textbox_xpath)))
        element.send_keys(lastname)

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
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath)))
        element.click()

    def clickCancelbutton(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancel_button_xpath)))
        element.click()
