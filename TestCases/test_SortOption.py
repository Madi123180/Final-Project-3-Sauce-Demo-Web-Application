from Pages.LoginPage import LoginPage  #imported POM file
from selenium.webdriver.support.wait import WebDriverWait
from Pages.SortOption import SortOption


#TC09
def test_sort_items(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)
    login.enter_username("standard_user")  # Method called to enter username
    login.enter_password("secret_sauce")  # Method called to enter password
    login.login_button_click()      #Method called to click on login button

    sort=SortOption(driver)  #creating object

    items=[sort.backpack_visible(),     #creating list to verify the index
    sort.bike_light_visible(),
    sort.bolt_tshirt_visible(),
    sort.fleece_jacket_visible(),
    sort.onesie_visible(),
    sort.tshirt_red_visible()]

    #validating the index position before clicking the sort options
    backpack = items.index(sort.backpack_visible())
    print(f"backpack position is: {backpack}")
    bike_light = items.index(sort.bike_light_visible())
    print(f"bike light position is: {bike_light}")
    bolt_tshirt = items.index(sort.bolt_tshirt_visible())
    print(f"bolt tshirt position is: {bolt_tshirt}")
    fleece = items.index(sort.fleece_jacket_visible())
    print(f"fleece jacket position is: {fleece}")
    onesie = items.index(sort.onesie_visible())
    print(f"onesie position is: {onesie}")
    red_tshirt = items.index(sort.tshirt_red_visible())
    print(f"red tshirt position is: {red_tshirt}")

    sort.click_sort() #clicking on sort option to Price low to high

    #again validating whether items are moved to the correct index position
    backpack = items.index(sort.backpack_visible())
    assert backpack == 4
    print("\nbackpack item is moved as expected")
    bike_light = items.index(sort.bike_light_visible())
    assert bike_light == 1
    print("bikelight item is moved as expected")
    bolt_tshirt = items.index(sort.bolt_tshirt_visible())
    assert bolt_tshirt == 2
    print("bolt_tshirt item is moved as expected")
    fleece = items.index(sort.fleece_jacket_visible())
    assert fleece == 5
    print("fleece item is moved as expected")
    onesie = items.index(sort.onesie_visible())
    assert onesie == 0
    print("onesie item is moved as expected")
    red_tshirt = items.index(sort.tshirt_red_visible())
    assert red_tshirt == 3
    print("red_tshirt item is moved as expected")

    sort.click_alphabet_sort() #changing sort option to Z to A

    ##again validating whether items are moved to the correct index position
    backpack = items.index(sort.backpack_visible())
    assert backpack == 5
    print(f"\nbackpack item is moved to position {backpack}")
    bike_light = items.index(sort.bike_light_visible())
    assert bike_light == 4
    print(f"bike_light item is moved to position {bike_light}")
    bolt_tshirt = items.index(sort.bolt_tshirt_visible())
    assert bolt_tshirt == 3
    print(f"bolt_tshirt item is moved to position {bolt_tshirt}")
    fleece = items.index(sort.fleece_jacket_visible())
    assert fleece == 2
    print(f"fleece item is moved to position {fleece}")
    onesie = items.index(sort.onesie_visible())
    assert onesie == 1
    print(f"onesie item is moved to position {onesie}")
    red_tshirt = items.index(sort.tshirt_red_visible())
    assert red_tshirt == 0
    print(f"red_tshirt item is moved to position {red_tshirt}")









