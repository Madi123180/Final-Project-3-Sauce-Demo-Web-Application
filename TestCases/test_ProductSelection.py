import time
from tkinter.font import names

from Pages.LoginPage import LoginPage  #imported POM file
from Pages.Logout import Logout  #imported POM file
from Pages.AddProductToCart import AddProductToCart
from Pages.ProductSelection import ProductSelection
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TC04 & TC05
def test_product_selection(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)
    login.enter_username("standard_user")  # Method called to enter username
    login.enter_password("secret_sauce")  # Method called to enter password
    login.login_button_click()      #Method called to click on login button
    time.sleep(2)

    # TC04  Validating whether cart icon is visible after the login
    wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='shopping_cart_link']")))
    print("\n Cart icon is visible")

    #TC05:  fetching their names and prices.
    #selecting 4 products and clicking add to cart button
    select=ProductSelection(driver)
    print("\n ** Printing Product name and Price ** \n")
    select.click_img_bike_light()
    print(f"Product name is: {select.bike_light_name().text} and Price is: {select.bike_light_price().text}")
    select.click_back()
    select.click_img_backpack()
    print(f"Product name is: {select.backpack_name().text} and Price is: {select.backpack_price().text}")
    select.click_back()
    select.click_img_red_tshirt()
    print(f"Product name is: {select.tshirt_red_name().text} and Price is: {select.tshirt_red_price().text}")
    select.click_back()
    select.click_img_bolt_tshirt()
    print(f"Product name is: {select.bolt_tshirt_name().text} and Price is: {select.bolt_tshirt_price().text}")
    select.click_back()

    #Logging out
    logout = Logout(driver)
    time.sleep(2)
    logout.click_menu()
    time.sleep(2)
    logout.click_logout()  # Method called to click logout option
