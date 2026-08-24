import os
from tkinter.font import names

from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Locaters
class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button="checkout"
        self.fname="first-name"
        self.lname="last-name"
        self.zip="postal-code"
        self.continue_button="continue"
        self.finish_button="finish"
        self.wait = WebDriverWait(self.driver, 10)

    def click_checkout_button(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.checkout_button))).click()

    def enter_fname(self,firstname): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.fname))).send_keys(firstname)

    def enter_lname(self,lastname): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.lname))).send_keys(lastname)

    def enter_zip(self,postalcode): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.zip))).send_keys(postalcode)

    def click_continue_button(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.continue_button))).click()

    def click_finish_button(self): # function to click on bike light product
        self.wait.until(EC.presence_of_element_located((By.ID, self.finish_button))).click()



















