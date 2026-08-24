from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class ResetApp:
    def __init__(self, driver):
        self.driver = driver
        self.reset_app="//a[@class='bm-item menu-item' and text()='Reset App State']"
        self.wait = WebDriverWait(self.driver, 10)

    def click_reset_option(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.reset_app))).click()





