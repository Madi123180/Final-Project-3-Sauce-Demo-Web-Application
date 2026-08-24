import time
from selenium.common import NoSuchElementException, TimeoutException
from UTIL import XLUtils
import datetime #imported this module to find the Date and Time of the day
import getpass #this is used fetch the user who is running the testcases
from Pages.LoginPage import LoginPage  #imported POM file
from Pages.Logout import Logout  #imported POM file

#TC01
def test_login(setup_driver):  #Pytest testcase
    #created conftest file open browser and launch the url
    driver  = setup_driver
    #Path of the excel test data sheet file from the local system
    path = "D://Malathi ID Proofs/Guvi/FP3Data.xlsx"

    #Finding date
    curdate = dt = datetime.date.today()

    #finding username of the executed scripts
    tester = getpass.getuser()

    #fetching total row count from the excel
    rows = XLUtils.get_row_count(path, 'Sheet1')


    #Used for loop to enter all the username and password in a single run
    for r in range(2, rows + 1):

        username = XLUtils.read_data(path, 'Sheet1', r, 5) #finding username field
        password = XLUtils.read_data(path, 'Sheet1', r, 6) #finding password field


        try:
            #Object created for LoginPage class from POM file
            login = LoginPage(driver)
            login.enter_username(username) #Method called to enter username
            login.enter_password(password) #Method called to enter password
            login.login_button_click() #Method called to click login button


            # once user logged in successfully below message will be printed in console
            print("Testcase Passed")

            #Writing result, user who is running the testcase and date into the test data excel sheet
            XLUtils.write_data(path, 'Sheet1', r, 7, "Test Passed", 4, curdate,3,tester)

            #TC03
            # Object created for LogoutPage class from POM file
            logout = Logout(driver)
            logout.click_menu()
            time.sleep(2)
            logout.click_logout() #Method called to click logout option
            assert 'Swag Labs' in driver.title

        # Exception added here, when login is not successful and when below exceptions are occurred
        # below message will be printed in the console and in the excel sheet.
        except(NoSuchElementException, TimeoutException):
            print("Testcase Failed")
            XLUtils.write_data(path, 'Sheet1', r, 7, 'Testcase failed', 4, curdate,3,tester)
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # super class exception: when the expected exceptions are not occurred below exception will work
        # {e} will print the exact message of the exception in console window
        except Exception as e:
            print(f"Login Failed: {e}")
            XLUtils.write_data(path, 'Sheet1', r, 7, 'Test Failed', 4, curdate,3,tester)
            driver.refresh()
            driver.quit()






