from selenium.webdriver.common.by import By
from pages.base_page import BasePage
 # REGION_LIST = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
class SbisContactsPage(BasePage):
    REGION_DROPDOWN =(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    PARTNERS_LIST = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]")
    CURRENT_REGION = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    TENSOR_BANNER = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a")
    def get_region(self):
        return self.driver.find_element(*self.CURRENT_REGION).text

    def change_region(self):
        self.click(*self.REGION_DROPDOWN)
        region_option = (By.XPATH, f"/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span") 
        self.click(*region_option)

    def is_partners_list_displayed(self):
        return self.is_visible(*self.PARTNERS_LIST)

    def is_partners_list_updated(self):
        return self.is_visible(*self.PARTNERS_LIST)

    def click_tensor_banner(self):
        self.click(*self.TENSOR_BANNER)