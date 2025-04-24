from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, by, locator):
        elm = self.wait.until(EC.element_to_be_clickable((by,locator)))
        elm.click()
        
    def is_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
    
    def get_elements(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))