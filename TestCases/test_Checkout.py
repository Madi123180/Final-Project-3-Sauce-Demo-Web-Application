import base64
import time
from Pages.LoginPage import LoginPage  #imported POM file
from Pages.Logout import Logout  #imported POM file
from Pages.AddProductToCart import AddProductToCart
from Pages.Checkout import Checkout
from selenium.webdriver.support.wait import WebDriverWait
from conftest import setup_driver


#TC08
def test_checkout(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)
    login.enter_username("standard_user")  # Method called to enter username
    login.enter_password("secret_sauce")  # Method called to enter password
    login.login_button_click()      #Method called to click on login button

    #Clicking add to cart button
    product=AddProductToCart(driver)
    product.click_bike_light()
    product.click_bolt_tshirt()
    product.click_tshirt_red()
    product.click_backpack()

    #click on cart icon
    product.click_cart_icon()

    checkout=Checkout(driver) #object created
    #clicking checkout button
    checkout.click_checkout_button()

    #Entering user details
    checkout.enter_fname("Guvi")
    checkout.enter_lname("User")
    checkout.enter_zip("554433")

    #clicking on continue button
    checkout.click_continue_button()

    #taking the total width and height of the webpage using body html tag
    dimensions = driver.execute_script("""
        return {
            width: Math.max(
                document.body.scrollWidth,          
                document.documentElement.scrollWidth
            ),
            height: Math.max(
                document.body.scrollHeight,
                document.documentElement.scrollHeight
            )
        };
    """)

    # using cdp to capture the entire part of the webpage, or normal selenium built in code will capture only
    # visible part
    result = driver.execute_cdp_cmd(
        "Page.captureScreenshot",
        {
            "format": "png",
            "captureBeyondViewport": True,      #telling tool to take the screenshot of full page
            "fromSurface": True,
            "clip": {
                "x": 0,         #this refers the left corner of the page
                "y": 0,         #this refers the top of the page
                "width": dimensions["width"],       #width of the entire webpage
                "height": dimensions["height"],     #height of the entire webpage
                "scale": 1
            }
        }
    )


    with open("order summary page.png", "wb") as file:
        file.write(base64.b64decode(result["data"]))


    #clicking on finish button
    checkout.click_finish_button()

    #verifying success message
    assert "Thank you for your order!" in driver.page_source


    #Logging out
    logout = Logout(driver)
    time.sleep(2)
    logout.click_menu()
    time.sleep(2)
    logout.click_logout()  # Method called to click logout option

