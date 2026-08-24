import time
from Pages.LoginPage import LoginPage  #imported POM file
from Pages.Logout import Logout  #imported POM file
from Pages.AddProductToCart import AddProductToCart
from Pages.ProductSelection import ProductSelection
from Pages.ResetAppState import ResetApp
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait


#TC10
def test_Reset(setup_driver):
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

    #clicking menu option
    logout=Logout(driver)
    logout.click_menu()
    time.sleep(3)

    #clicking ResetAppStore option from menu
    reset=ResetApp(driver)
    reset.click_reset_option()
    driver.refresh()


    #Verifying items are removed from the page after clicking the ResetAppStore option
    print("\n **Verifying items are removed **")
    Bike_Light=driver.find_elements(By.XPATH,"//div[text()='Sauce Labs Bike Light']")
    Bolt_tShirt=driver.find_elements(By.XPATH,"//div[text()='Sauce Labs Bolt T-Shirt']")
    if not Bike_Light and not Bolt_tShirt:
        print("items are removed")
    else:
        print("item is listed")








