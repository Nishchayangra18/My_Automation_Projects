from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage:
    PIM_menu_button_xpath = "(//a[@class='oxd-main-menu-item'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickPIM(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.PIM_menu_button_xpath)))
        element.click()

