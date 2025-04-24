from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorAboutPage(BasePage):
    WORKING_SECTION_IMAGES = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img")

    def get_images_size(self):
        images = self.get_elements(*self.WORKING_SECTION_IMAGES)
        return [(img.size['width'], img.size['height']) for img in images]