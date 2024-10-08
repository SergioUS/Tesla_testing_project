# Unittest, includes Positive and Negative tests for Tesla site, Shop vehicle Accessories for Model X
# prepared by Dmitry Antipenko

import random
import time
import unittest

#import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import Helpers_Shop_Vehicle_Accessories_Model_X as H

faker = Faker()


# driver sleep from 1 to 5 seconds
def delay():
    time.sleep(random.randint(1, 5))


#def scroll_to_element(iframe):
#    pass

class ChromePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        self.driver.maximize_window()


    # Test Case 061: Verify that "Shop" button clickable in the main page and transfer to correct page
    def test_case_061(self):
        driver = self.driver
        print("Test Case 061")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link)
        VehicleAccessories_menu.click()

        delay()

        # Check if the new window title contains "Vehicle Accessories"
        if "Vehicle Accessories" not in driver.title:
            raise Exception("Vehicle Accessories - Test Case 061 failed")
        else:
            print("Vehicle Accessories is available - Test Case 061 passed")

        delay()


    # Test case 062: Verify that  button "Model X Pet Liner" page is visible in the header and link is clickable
    def test_case_062(self):
        driver = self.driver
        print("Test Case 062")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Pet Liner"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(5)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(4)


        # Verify that the Vehicle Accessories Model X Pet Liner page is loaded by checking URL or page title
        self.assertIn("model-x-pet-liner", driver.current_url.lower(), "Vehicle Accessories Model X Pet Liner page not loaded")

        delay()


    # Test case 063: Verify that item "Model X Key Fob" can be added to cart.
    def test_case_063(self):
        driver = self.driver
        print("Test Case 063")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)


        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()


    # Test case 064: Verify that item "Model X Powered By the Sun License Plate Frame" can be added to cart.
    def test_case_064(self):
        driver = self.driver
        print("Test Case 064")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Car Cover"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        LPF_link = driver.find_element(By.XPATH, H.LPF_link)
        LPF_link.click()

        time.sleep(2)

        # Choose quantity (2)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)


        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 064 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 064 failed")

        delay()


    # Test case 065: Verify that when you click on "Model X", a catalog with accessories for the "Tesla Model X" opens and works
    def test_case_065(self):
        driver = self.driver
        print("Test Case 065")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1000)")
        delay()
        driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,2000)")
        delay()
        driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,3000)")
        delay()
        driver.execute_script("window.scrollTo(0,4000)")
        delay()
        driver.execute_script("window.scrollTo(0,5000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,6000)")
        delay()
        driver.execute_script("window.scrollTo(0,7000)")
        delay()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Verify that when you click on "Model X", a catalog with accessories for the "Vehicle Accessories Model X" opens and works
        self.assertIn("model-x", driver.current_url.lower(), "Vehicle Accessories Model X opens and works")

        delay()


    def tearDown(self):
        self.driver.quit()



class ChromeNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        self.driver.maximize_window()


    # Test case 061_61: Verify that user can't buy "9" quantity item.
    def test_case_061_61(self):
        driver = self.driver
        print("Test Case 061_61")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(1)

        # Choose quantity (9)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("9")

        time.sleep(0.5)

        # Convert 9 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")


        price  = driver.find_element(By.XPATH, "(//p[@data-colorkey='1819444-00-A'])[1]").text
        print("Current Key fob price is:", price)
        if price == "$175":
            print("Price is OK $175")
        else:
            print("Price is Different. Current Key fob price is:", price)


        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 9 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print("User can't buy 9 quantity item and field automatically converted number to 2 - Test Case 061_61 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 061_61 failed")


    # Test case 062_62: Verify that user has not entered Email in the line "Email" when appointment a Demo Drive.
    def test_case_062_62(self):
        driver = self.driver
        print("Test Case 062_62")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Vehicle"
        Vehicle_menu = driver.find_element(By.XPATH, H.Vehicle_link)

        delay()

        actions = ActionChains(driver)
        actions.move_to_element(Vehicle_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, Vehicle_menu)

        time.sleep(2)

        VehicleModelX = driver.find_element(By.XPATH, H.VehicleModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleModelX).click().perform()

        time.sleep(4)

        DemoDriveX = driver.find_element(By.XPATH, H.Demo_Drive_X_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX).click().perform()

        time.sleep(3)

        DemoDriveX_Schedule = driver.find_element(By.XPATH, H.Demo_Drive_X_Schedule_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX_Schedule).click().perform()

        time.sleep(3)



        # Appointment for a test drive.
        FN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN_link)))
        FN_link.clear()
        FN_link.send_keys("Dmitry")
        LN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN_link)))
        LN_link.clear()
        LN_link.send_keys("Lan")
        PN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.PN_link)))
        PN_link.clear()
        PN_link.send_keys("777-777-7777")
        driver.find_element(By.XPATH, H.Submit).click()
        time.sleep(3)

        registration_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.Submit)))

        self.assertTrue(registration_form.is_displayed(), "Appointment for a test drive")
        if registration_form.is_displayed():
            print("Required input field - Test Case 062_62 passed")
        else:
            raise Exception("You have an appointment - Test Case 062_62 failed")

        delay()


    # Test case 063_63: Validate that user is unable to buy Mud Flaps by not entering an Email.
    def test_case_063_63(self):
        driver = self.driver
        print("Test Case 063_63")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, VehicleAccessories_menu)
        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()
        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()
        time.sleep(2)

        # Choose quantity (2) and click Add to Card
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")
        time.sleep(3)

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        time.sleep(5)

        # Click Checkout
        driver.find_element(By.XPATH, H.Checkout).click()
        time.sleep(3)

        # Not enter email address and click on the button "Continue as Guest"
        driver.find_element(By.XPATH, H.Continue2).click()
        time.sleep(3)

        # Fill out the guest form
        FN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN2_link)))
        FN2_link.clear()
        FN2_link.send_keys("Dmitry")
        time.sleep(2)
        LN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN2_link)))
        LN2_link.clear()
        LN2_link.send_keys("Lan")
        time.sleep(3)
        driver.find_element(By.XPATH, H.Next2_link).click()
        time.sleep(5)

        # Make sure this item added to cart
        by_mun_flaps_confirmation = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.Next2_link)))

        self.assertTrue(by_mun_flaps_confirmation.is_displayed(), "Button Next")
        if by_mun_flaps_confirmation.is_displayed():
            print(
                'The user not entered an email, a message appeared "Please populate this field - Email" - Test Case 063_63 passed')
        else:
            raise Exception("Button Next - Test Case 063_63 failed")
        delay()


    # Test case 064_64: Verify that user can't buy "4" quantity item.
    def test_case_064_64(self):
        driver = self.driver
        print("Test Case 064_64")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()

        time.sleep(2)

        # Choose quantity (4)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("4")

        time.sleep(3)

        # Convert 4 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 4 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print(
                "User can't buy 4 quantity item and field automatically converted number to 2 - Test Case 064_64 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 064_64 failed")
        delay()


    # Test case 065_65: Verify that user can added wrong information in Search Line.
    def test_case_065_65(self):
        driver = self.driver
        print("Test Case 065_65")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X "
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        S_L_ModelX = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        action = ActionChains(driver)
        action.move_to_element(S_L_ModelX).click().perform()

        time.sleep(2)

        # Enter “&sp4” in Search Line.
        S_L_ModelX = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.S_l_ModelX_link)))
        S_L_ModelX.clear()
        search_bar = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        time.sleep(2)
        search_bar.send_keys("&sp4")
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        delay()

        # Make sure it is transfer to correct page.
        assert "https://shop.tesla.com/search?searchTerm=%26sp4" in driver.current_url
        print("No Results Found.")
        print("The search engine didn't allow us to enter incorrect information - Test Case 06_65 passed")
        time.sleep(4)


    def tearDown(self):
        self.driver.quit()



class FirefoxPositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    # Test Case 061: Verify that "Shop" button clickable in the main page and transfer to correct page
    def test_case_061(self):
        driver = self.driver
        print("Test Case 061")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link)
        VehicleAccessories_menu.click()

        delay()

        # Check if the new window title contains "Vehicle Accessories"
        if "Vehicle Accessories" not in driver.title:
            raise Exception("Vehicle Accessories - Test Case 061 failed")
        else:
            print("Vehicle Accessories is available - Test Case 061 passed")

        delay()

    # Test case 062: Verify that  button "Model X Pet Liner" page is visible in the header and link is clickable
    def test_case_062(self):
        driver = self.driver
        print("Test Case 062")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Pet Liner"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(5)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(4)

        # Verify that the Vehicle Accessories Model X Pet Liner page is loaded by checking URL or page title
        self.assertIn("model-x-pet-liner", driver.current_url.lower(),
                      "Vehicle Accessories Model X Pet Liner page not loaded")

        delay()

    # Test case 063: Verify that item "Model X Key Fob" can be added to cart.
    def test_case_063(self):
        driver = self.driver
        print("Test Case 063")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)

        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()

    # Test case 064: Verify that item "Model X Powered By the Sun License Plate Frame" can be added to cart.
    def test_case_064(self):
        driver = self.driver
        print("Test Case 064")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Car Cover"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        LPF_link = driver.find_element(By.XPATH, H.LPF_link)
        LPF_link.click()

        time.sleep(2)

        # Choose quantity (2)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)

        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 064 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 064 failed")

        delay()

    # Test case 065: Verify that when you click on "Model X", a catalog with accessories for the "Tesla Model X" opens and works
    def test_case_065(self):
        driver = self.driver
        print("Test Case 065")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1000)")
        delay()
        driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,2000)")
        delay()
        driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,3000)")
        delay()
        driver.execute_script("window.scrollTo(0,4000)")
        delay()
        driver.execute_script("window.scrollTo(0,5000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,6000)")
        delay()
        driver.execute_script("window.scrollTo(0,7000)")
        delay()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Verify that when you click on "Model X", a catalog with accessories for the "Vehicle Accessories Model X" opens and works
        self.assertIn("model-x", driver.current_url.lower(), "Vehicle Accessories Model X opens and works")

        delay()

    def tearDown(self):
        self.driver.quit()



class FirefoxNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()


    # Test case 061_61: Verify that user can't buy "9" quantity item.
    def test_case_061_61(self):
        driver = self.driver
        print("Test Case 061_61")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(1)

        # Choose quantity (9)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("9")

        time.sleep(0.5)

        # Convert 9 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")


        price  = driver.find_element(By.XPATH, "(//p[@data-colorkey='1819444-00-A'])[1]").text
        print("Current Key fob price is:", price)
        if price == "$175":
            print("Price is OK $175")
        else:
            print("Price is Different. Current Key fob price is:", price)


        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 9 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print("User can't buy 9 quantity item and field automatically converted number to 2 - Test Case 061_61 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 061_61 failed")


    # Test case 062_62: Verify that user has not entered Email in the line "Email" when appointment a Demo Drive.
    def test_case_062_62(self):
        driver = self.driver
        print("Test Case 062_62")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Vehicle"
        Vehicle_menu = driver.find_element(By.XPATH, H.Vehicle_link)

        delay()

        actions = ActionChains(driver)
        actions.move_to_element(Vehicle_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, Vehicle_menu)

        time.sleep(2)

        VehicleModelX = driver.find_element(By.XPATH, H.VehicleModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleModelX).click().perform()

        time.sleep(4)

        DemoDriveX = driver.find_element(By.XPATH, H.Demo_Drive_X_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX).click().perform()

        time.sleep(3)

        DemoDriveX_Schedule = driver.find_element(By.XPATH, H.Demo_Drive_X_Schedule_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX_Schedule).click().perform()

        time.sleep(3)



        # Appointment for a test drive.
        FN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN_link)))
        FN_link.clear()
        FN_link.send_keys("Dmitry")
        LN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN_link)))
        LN_link.clear()
        LN_link.send_keys("Lan")
        PN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.PN_link)))
        PN_link.clear()
        PN_link.send_keys("777-777-7777")
        driver.find_element(By.XPATH, H.Submit).click()
        time.sleep(3)

        registration_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.Submit)))

        self.assertTrue(registration_form.is_displayed(), "Appointment for a test drive")
        if registration_form.is_displayed():
            print("Required input field - Test Case 062_62 passed")
        else:
            raise Exception("You have an appointment - Test Case 062_62 failed")

        delay()


    # Test case 063_63: Validate that user is unable to buy Mud Flaps by not entering an Email.
    def test_case_063_63(self):
        driver = self.driver
        print("Test Case 063_63")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, VehicleAccessories_menu)
        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()
        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()
        time.sleep(2)

        # Choose quantity (2) and click Add to Card
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")
        time.sleep(3)

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        time.sleep(5)

        # Click Checkout
        driver.find_element(By.XPATH, H.Checkout).click()
        time.sleep(3)

        # Not enter email address and click on the button "Continue as Guest"
        driver.find_element(By.XPATH, H.Continue2).click()
        time.sleep(3)

        # Fill out the guest form
        FN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN2_link)))
        FN2_link.clear()
        FN2_link.send_keys("Dmitry")
        time.sleep(2)
        LN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN2_link)))
        LN2_link.clear()
        LN2_link.send_keys("Lan")
        time.sleep(3)
        driver.find_element(By.XPATH, H.Next2_link).click()
        time.sleep(5)

        # Make sure this item added to cart
        by_mun_flaps_confirmation = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.Next2_link)))

        self.assertTrue(by_mun_flaps_confirmation.is_displayed(), "Button Next")
        if by_mun_flaps_confirmation.is_displayed():
            print(
                'The user not entered an email, a message appeared "Please populate this field - Email" - Test Case 063_63 passed')
        else:
            raise Exception("Button Next - Test Case 063_63 failed")
        delay()


    # Test case 064_64: Verify that user can't buy "4" quantity item.
    def test_case_064_64(self):
        driver = self.driver
        print("Test Case 064_64")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()

        time.sleep(2)

        # Choose quantity (4)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("4")

        time.sleep(3)

        # Convert 4 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 4 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print(
                "User can't buy 4 quantity item and field automatically converted number to 2 - Test Case 064_64 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 064_64 failed")
        delay()


    # Test case 065_65: Verify that user can added wrong information in Search Line.
    def test_case_065_65(self):
        driver = self.driver
        print("Test Case 065_65")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X "
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        S_L_ModelX = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        action = ActionChains(driver)
        action.move_to_element(S_L_ModelX).click().perform()

        time.sleep(2)

        # Enter “&sp4” in Search Line.
        S_L_ModelX = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.S_l_ModelX_link)))
        S_L_ModelX.clear()
        search_bar = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        time.sleep(2)
        search_bar.send_keys("&sp4")
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        delay()

        # Make sure it is transfer to correct page.
        assert "https://shop.tesla.com/search?searchTerm=%26sp4" in driver.current_url
        print("No Results Found.")
        print("The search engine didn't allow us to enter incorrect information - Test Case 06_65 passed")
        time.sleep(4)


    def tearDown(self):
        self.driver.quit()



class EdgePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()


    # Test Case 061: Verify that "Shop" button clickable in the main page and transfer to correct page
    def test_case_061(self):
        driver = self.driver
        print("Test Case 061")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link)
        VehicleAccessories_menu.click()

        delay()

        # Check if the new window title contains "Vehicle Accessories"
        if "Vehicle Accessories" not in driver.title:
            raise Exception("Vehicle Accessories - Test Case 061 failed")
        else:
            print("Vehicle Accessories is available - Test Case 061 passed")

        delay()


    # Test case 062: Verify that  button "Model X Pet Liner" page is visible in the header and link is clickable
    def test_case_062(self):
        driver = self.driver
        print("Test Case 062")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Pet Liner"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(5)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(4)


        # Verify that the Vehicle Accessories Model X Pet Liner page is loaded by checking URL or page title
        self.assertIn("model-x-pet-liner", driver.current_url.lower(), "Vehicle Accessories Model X Pet Liner page not loaded")

        delay()


    # Test case 063: Verify that item "Model X Key Fob" can be added to cart.
    def test_case_063(self):
        driver = self.driver
        print("Test Case 063")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)


        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()


    # Test case 064: Verify that item "Model X Powered By the Sun License Plate Frame" can be added to cart.
    def test_case_064(self):
        driver = self.driver
        print("Test Case 064")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Car Cover"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        LPF_link = driver.find_element(By.XPATH, H.LPF_link)
        LPF_link.click()

        time.sleep(2)

        # Choose quantity (2)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)


        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 064 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 064 failed")

        delay()


    # Test case 065: Verify that when you click on "Model X", a catalog with accessories for the "Tesla Model X" opens and works
    def test_case_065(self):
        driver = self.driver
        print("Test Case 065")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1000)")
        delay()
        driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,2000)")
        delay()
        driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,3000)")
        delay()
        driver.execute_script("window.scrollTo(0,4000)")
        delay()
        driver.execute_script("window.scrollTo(0,5000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,6000)")
        delay()
        driver.execute_script("window.scrollTo(0,7000)")
        delay()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Verify that when you click on "Model X", a catalog with accessories for the "Vehicle Accessories Model X" opens and works
        self.assertIn("model-x", driver.current_url.lower(), "Vehicle Accessories Model X opens and works")

        delay()


    def tearDown(self):
        self.driver.quit()



class EdgeNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--lang=en-US')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()


    # Test case 061_61: Verify that user can't buy "9" quantity item.
    def test_case_061_61(self):
        driver = self.driver
        print("Test Case 061_61")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Key Fob"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        KeyFob_link = driver.find_element(By.XPATH, H.KeyFob_link)
        KeyFob_link.click()

        time.sleep(1)

        # Choose quantity (9)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("9")

        time.sleep(0.5)

        # Convert 9 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")


        price  = driver.find_element(By.XPATH, "(//p[@data-colorkey='1819444-00-A'])[1]").text
        print("Current Key fob price is:", price)
        if price == "$175":
            print("Price is OK $175")
        else:
            print("Price is Different. Current Key fob price is:", price)


        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 9 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print("User can't buy 9 quantity item and field automatically converted number to 2 - Test Case 061_61 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 061_61 failed")


    # Test case 062_62: Verify that user has not entered Email in the line "Email" when appointment a Demo Drive.
    def test_case_062_62(self):
        driver = self.driver
        print("Test Case 062_62")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Vehicle"
        Vehicle_menu = driver.find_element(By.XPATH, H.Vehicle_link)

        delay()

        actions = ActionChains(driver)
        actions.move_to_element(Vehicle_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, Vehicle_menu)

        time.sleep(2)

        VehicleModelX = driver.find_element(By.XPATH, H.VehicleModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleModelX).click().perform()

        time.sleep(4)

        DemoDriveX = driver.find_element(By.XPATH, H.Demo_Drive_X_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX).click().perform()

        time.sleep(3)

        DemoDriveX_Schedule = driver.find_element(By.XPATH, H.Demo_Drive_X_Schedule_link)
        action = ActionChains(driver)
        action.move_to_element(DemoDriveX_Schedule).click().perform()

        time.sleep(3)



        # Appointment for a test drive.
        FN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN_link)))
        FN_link.clear()
        FN_link.send_keys("Dmitry")
        LN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN_link)))
        LN_link.clear()
        LN_link.send_keys("Lan")
        PN_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.PN_link)))
        PN_link.clear()
        PN_link.send_keys("777-777-7777")
        driver.find_element(By.XPATH, H.Submit).click()
        time.sleep(3)

        registration_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.Submit)))

        self.assertTrue(registration_form.is_displayed(), "Appointment for a test drive")
        if registration_form.is_displayed():
            print("Required input field - Test Case 062_62 passed")
        else:
            raise Exception("You have an appointment - Test Case 062_62 failed")

        delay()


    # Test case 063_63: Validate that user is unable to buy Mud Flaps by not entering an Email.
    def test_case_063_63(self):
        driver = self.driver
        print("Test Case 063_63")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                            var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                            arguments[0].dispatchEvent(event);
                            """
        driver.execute_script(hover_script, VehicleAccessories_menu)
        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()
        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()
        time.sleep(2)

        # Choose quantity (2) and click Add to Card
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")
        time.sleep(3)

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        time.sleep(5)

        # Click Checkout
        driver.find_element(By.XPATH, H.Checkout).click()
        time.sleep(3)

        # Not enter email address and click on the button "Continue as Guest"
        driver.find_element(By.XPATH, H.Continue2).click()
        time.sleep(3)

        # Fill out the guest form
        FN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.FN2_link)))
        FN2_link.clear()
        FN2_link.send_keys("Dmitry")
        time.sleep(2)
        LN2_link = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.LN2_link)))
        LN2_link.clear()
        LN2_link.send_keys("Lan")
        time.sleep(3)
        driver.find_element(By.XPATH, H.Next2_link).click()
        time.sleep(5)

        # Make sure this item added to cart
        by_mun_flaps_confirmation = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.Next2_link)))

        self.assertTrue(by_mun_flaps_confirmation.is_displayed(), "Button Next")
        if by_mun_flaps_confirmation.is_displayed():
            print(
                'The user not entered an email, a message appeared "Please populate this field - Email" - Test Case 063_63 passed')
        else:
            raise Exception("Button Next - Test Case 063_63 failed")
        delay()


    # Test case 064_64: Verify that user can't buy "4" quantity item.
    def test_case_064_64(self):
        driver = self.driver
        print("Test Case 064_64")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X Mud Flaps"
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        driver.execute_script("window.scrollTo(0,4000)")
        MudFlaps_link = driver.find_element(By.XPATH, H.MudFlaps_link)
        MudFlaps_link.click()

        time.sleep(2)

        # Choose quantity (4)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("4")

        time.sleep(3)

        # Convert 4 to 2 by clicking outside the of filed
        driver.find_element(By.XPATH, "//header/div[@id='mainMenu']/ol[1]").click()

        delay()

        field_num = driver.find_element(By.XPATH, "//input[@id='3']").get_attribute("value")
        print(field_num)

        if field_num == "2":
            print("Qty is OK")
        else:
            print("QTY is NOT OK")

        price = driver.find_element(By.XPATH, H.MudFlapsPrice_link).text
        print("Current Key fob price is:", price)
        if price == "$40":
            print("Price is OK $40")
        else:
            print("Price is Different. Current Key fob price is:", price)

        # Make sure this item added to cart
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Make sure Quantity 4 added to cart")
        if add_to_cart_confirmation.is_displayed():
            print(
                "User can't buy 4 quantity item and field automatically converted number to 2 - Test Case 064_64 passed")
        else:
            raise Exception("User can buy item more then 2 - Test Case 064_64 failed")
        delay()


    # Test case 065_65: Verify that user can added wrong information in Search Line.
    def test_case_065_65(self):
        driver = self.driver
        print("Test Case 065_65")

        # Opening Tesla site
        driver.get(H.tesla_url)

        delay()

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()

        delay()

        # Click on the header menu "Vehicle Accessories"
        VehicleAccessories_menu = driver.find_element(By.XPATH, H.VehicleAccessories_link2)

        delay()

        # Navigate on the header menu "Vehicle Accessories" and click on the link "Model X "
        actions = ActionChains(driver)
        actions.move_to_element(VehicleAccessories_menu).perform()
        hover_script = """
                        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                        arguments[0].dispatchEvent(event);
                        """
        driver.execute_script(hover_script, VehicleAccessories_menu)

        time.sleep(3)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(4)

        S_L_ModelX = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        action = ActionChains(driver)
        action.move_to_element(S_L_ModelX).click().perform()

        time.sleep(2)

        # Enter “&sp4” in Search Line.
        S_L_ModelX = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.S_l_ModelX_link)))
        S_L_ModelX.clear()
        search_bar = driver.find_element(By.XPATH, H.S_l_ModelX_link)
        time.sleep(2)
        search_bar.send_keys("&sp4")
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        delay()

        # Make sure it is transfer to correct page.
        assert "https://shop.tesla.com/search?searchTerm=%26sp4" in driver.current_url
        print("No Results Found.")
        print("The search engine didn't allow us to enter incorrect information - Test Case 06_65 passed")
        time.sleep(4)


def teardown(self):
        self.driver.quit()


#if __name__ == "__main__":
#    unittest.main()
