from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#Locaters
class SortOption:
    def __init__(self, driver):
        self.driver = driver
        self.bike_light="(//div[@class='inventory_item_name '])[2]"
        self.bolt_tshirt="(//div[@class='inventory_item_name '])[3]"
        self.tshirt_red="(//div[@class='inventory_item_name '])[6]"
        self.backpack="(//div[@class='inventory_item_name '])[1]"
        self.fleece_jacket="(//div[@class='inventory_item_name '])[4]"
        self.onesie="(//div[@class='inventory_item_name '])[5]"
        self.sort_menu="//select[@class='product_sort_container']"

        self.wait = WebDriverWait(self.driver, 10)

    def backpack_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.backpack)))

    def bike_light_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.bike_light)))

    def bolt_tshirt_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.bolt_tshirt)))

    def fleece_jacket_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fleece_jacket)))

    def onesie_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.onesie)))

    def tshirt_red_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tshirt_red)))

    def click_sort(self):
        sort=self.wait.until(EC.presence_of_element_located((By.XPATH,self.sort_menu)))
        sort.click()
        options=Select(sort)
        options.select_by_visible_text("Price (low to high)")

    def click_alphabet_sort(self):
        sort=self.wait.until(EC.presence_of_element_located((By.XPATH,self.sort_menu)))
        sort.click()
        options=Select(sort)
        options.select_by_visible_text("Name (Z to A)")