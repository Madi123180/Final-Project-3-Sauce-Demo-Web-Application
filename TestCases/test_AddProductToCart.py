import time
from Pages.LoginPage import LoginPage  #imported POM file
from Pages.Logout import Logout  #imported POM file
from Pages.AddProductToCart import AddProductToCart
from Pages.ProductSelection import ProductSelection
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait


#TC06 & TC07
def test_add_items_to_cart(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)
    login.enter_username("standard_user")  # Method called to enter username
    login.enter_password("secret_sauce")  # Method called to enter password
    login.login_button_click()      #Method called to click on login button
    time.sleep(2)

    #Clicking add to cart button
    product=AddProductToCart(driver)
    product.click_bike_light()
    product.click_bolt_tshirt()
    product.click_tshirt_red()
    product.click_backpack()

    #click on cart icon
    product.click_cart_icon()

    select=ProductSelection(driver)

    #TC06
    #fetching items quanity from the cart
    item_count=driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
    if item_count == "4":       #making sure that count is showing as 4 using if condition
        print("\n Product quantity count is showing correctly")
    else:
        print("\n Product quantity count is showing incorrectly")

    #TC07
    #Validating whether the added items listed correct in checkout summary using text
    print("\n **Verifying Checkout page items using text **")
    if select.bike_light_name().text == 'Sauce Labs Bike Light':
        print("Bike Light item is displayed correctly in the checkout page")
    if select.bolt_tshirt_name().text == 'Sauce Labs Bolt T-Shirt':
        print("bolt_tshirt item is displayed correctly in the checkout page")
    if select.tshirt_red_name().text == 'Test.allTheThings() T-Shirt (Red)':
        print("tshirt_red item is displayed correctly in the checkout page")
    if select.backpack_name().text == 'Sauce Labs Backpack':
        print("backpack item is displayed correctly in the checkout page")

    #Logging out
    logout = Logout(driver)
    time.sleep(2)
    logout.click_menu()
    time.sleep(2)
    logout.click_logout()  # Method called to click logout option

def test_negative_add_incorrect_items(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)
    login.enter_username("standard_user")  # Method called to enter username
    login.enter_password("secret_sauce")  # Method called to enter password
    login.login_button_click()      #Method called to click on login button
    time.sleep(2)

    #Clicking add to cart button
    product=AddProductToCart(driver)
    product.click_bike_light()
    product.click_bolt_tshirt()

    #click on cart icon
    product.click_cart_icon()

    select=ProductSelection(driver)

    #TC06
    #fetching items quanity from the cart
    item_count=driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
    if item_count == "2":       #making sure that count is showing as 4 using if condition
        print("\n Product quantity count is showing correctly")
    else:
        print("\n Product quantity count is showing incorrectly")

    #TC07
    #Validating whether the added items listed correct in checkout summary using text
    print("\n **Verifying Checkout page items using text **")
    if select.bike_light_name().text == 'Sauce Labs Bolt T-Shirt':
        print("Bike Light item is displayed correctly in the checkout page")
    else:
        print("Product name is not matched")
    if select.bolt_tshirt_name().text == 'Sauce Labs Backpack':
        print("bolt_tshirt item is displayed correctly in the checkout page")
    else:
        print("Product name is not matched")

    #Logging out
    logout = Logout(driver)
    time.sleep(2)
    logout.click_menu()
    time.sleep(2)
    logout.click_logout()  # Method called to click logout option



