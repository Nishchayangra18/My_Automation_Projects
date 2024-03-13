from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    user_area_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 20)  # set a max wait time
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        element.click()

    def clickLogout(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.button_logout_linktext)))
        element.click()

    def clickuserdropdown(self):
        self.driver.find_element(By.XPATH, self.user_area_dropdown_xpath).click()
