from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorMainPage(BasePage):
    STRENGTH_IN_PEOPLE = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div")
    DETAILS_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a")

    def is_block_present(self):
        return self.is_visible(*self.STRENGTH_IN_PEOPLE)

    def click_more(self):
        self.click(*self.DETAILS_BUTTON)