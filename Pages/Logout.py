from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.menu = "react-burger-menu-btn"     #id to click on menu option
        self.logout="//a[@id='logout_sidebar_link']"    #xpath to click on logout option
        self.wait = WebDriverWait(self.driver, 10)

    def click_menu(self): #function to click on menu option and logout option
        self.wait.until(EC.presence_of_element_located((By.ID, self.menu))).click()

    def click_logout(self): #function to click on menu option and logout option
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.logout))).click()









