from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SbisMainPage(BasePage):
    CONTACTS_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div")
    CONTACTS_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]")
    
    def go_to_contacts(self):
         
        self.click(*self.CONTACTS_MENU_BUTTON)
        self.click(*self.CONTACTS_BUTTON)

