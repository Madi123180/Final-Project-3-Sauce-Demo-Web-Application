from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class ProductSelection:
    def __init__(self, driver):
        self.driver = driver
        self.img_backpack="//img[@alt='Sauce Labs Backpack']"
        self.img_bike_light="//img[@alt='Sauce Labs Bike Light']"
        self.img_bolt_tshirt="//img[@alt='Sauce Labs Bolt T-Shirt']"
        self.img_red_tshirt="//img[@alt='Test.allTheThings() T-Shirt (Red)']"
        self.name_bike_light = "//div[text()='Sauce Labs Bike Light']"
        self.name_bolt_tshirt = "//div[text()='Sauce Labs Bolt T-Shirt']"
        self.name_tshirt_red = "//div[text()='Test.allTheThings() T-Shirt (Red)']"
        self.name_backpack = "//div[text()='Sauce Labs Backpack']"
        self.price_bike_light = "//div[@class='inventory_details_price' and text()='$' and text()='9.99']"
        self.price_bolt_tshirt = "//div[@class='inventory_details_desc large_size']/following::div[text()='$' and text()='15.99']"
        self.price_tshirt_red = "//div[@class='inventory_details_desc large_size']/following::div[text()='$' and text()='15.99']"
        self.price_backpack = "//div[@class='inventory_details_price' and text()='$' and text()='29.99']"
        self.back="//img[@alt='Go back']"
        self.wait = WebDriverWait(self.driver, 10)

    def click_img_bike_light(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.img_bike_light))).click()

    def click_img_backpack(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.img_backpack))).click()

    def click_img_bolt_tshirt(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.img_bolt_tshirt))).click()

    def click_img_red_tshirt(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.img_red_tshirt))).click()

    def bike_light_name(self):  # function fetch text of the bike light product
        return self.driver.find_element(By.XPATH, self.name_bike_light)

    def bolt_tshirt_name(self):  # function fetch text of the bolt tshirt product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_bolt_tshirt)))

    def tshirt_red_name(self):  # function fetch text of the red t shirt product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_tshirt_red)))

    def backpack_name(self):  # function fetch text of the backpack product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_backpack)))

    def bike_light_price(self):  # function fetch price of the bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.price_bike_light)))
        return self.driver.find_element(By.XPATH, self.price_bike_light)

    def bolt_tshirt_price(self):  # function fetch price of the bolt tshirt product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.price_bolt_tshirt)))

    def tshirt_red_price(self):  # function fetch price of the red t shirt product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.price_tshirt_red)))

    def backpack_price(self):  # function fetch price of the backpack product
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.price_backpack)))

    def click_back(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.back))).click()
