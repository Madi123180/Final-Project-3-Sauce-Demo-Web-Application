from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class AddProductToCart:
    def __init__(self, driver):
        self.driver = driver
        self.bike_light="//button[@id='add-to-cart-sauce-labs-bike-light']"
        self.bolt_tshirt="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
        self.tshirt_red="//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
        self.backpack="//button[@id='add-to-cart-sauce-labs-backpack']"
        self.cart_icon="//a[@class='shopping_cart_link']"
        self.wait = WebDriverWait(self.driver, 10)

    def click_bike_light(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.bike_light))).click()

    def click_bolt_tshirt(self): # function to click on bolt tshirt product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.bolt_tshirt))).click()

    def click_tshirt_red(self):  # function to click on red tshirt product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.tshirt_red))).click()

    def click_backpack(self):  # function to click on backpack product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.backpack))).click()


    def click_cart_icon(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.cart_icon))).click()





