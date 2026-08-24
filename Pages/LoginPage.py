from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "user-name"   # id of username field
        self.password="password"       #id of password field
        self.login_button="//input[@id='login-button']"  #xpath to click on login button
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username(self,name): #function to enter username
        user= self.wait.until(EC.presence_of_element_located((By.ID, self.username)))
        user.send_keys(name)

    def enter_password(self,password): #function to enter password
        pwd= self.wait.until(EC.presence_of_element_located((By.ID, self.password)))
        pwd.send_keys(password)

    def login_button_click(self): #function to click on login button
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login_button))).click()








