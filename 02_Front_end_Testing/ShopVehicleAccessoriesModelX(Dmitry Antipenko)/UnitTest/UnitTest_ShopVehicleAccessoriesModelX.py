# Unittest, includes Positive and Negative tests for Tesla site, Shop vehicle Accessories for Model X
# prepared by Dmitry Antipenko

import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from faker import Faker
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

class ChromeAPositiveTests(unittest.TestCase):

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

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(5)


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

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()


    # Test case 064: Verify that item "Model X Car Cover" can be added to cart.
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
        CarCover_link = driver.find_element(By.XPATH, H.CarCover_link)
        CarCover_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

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

class FirefoxAPositiveTests(unittest.TestCase):

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

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(5)


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

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()


    # Test case 064: Verify that item "Model X Car Cover" can be added to cart.
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
        CarCover_link = driver.find_element(By.XPATH, H.CarCover_link)
        CarCover_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

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


class EdgeAPositiveTests(unittest.TestCase):

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

        time.sleep(2)

        VehicleAccessoriesModelX = driver.find_element(By.XPATH, H.VehicleAccessoriesModelX_link)
        action = ActionChains(driver)
        action.move_to_element(VehicleAccessoriesModelX).click().perform()

        time.sleep(3)

        driver.execute_script("window.scrollTo(0,2400)")

        delay()

        PetLiner_link = driver.find_element(By.XPATH, H.PetLiner_link)
        PetLiner_link.click()

        time.sleep(5)


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

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 063 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 063 failed")

        delay()


    # Test case 064: Verify that item "Model X Car Cover" can be added to cart.
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
        CarCover_link = driver.find_element(By.XPATH, H.CarCover_link)
        CarCover_link.click()

        time.sleep(2)

        # Choose quantity (1)
        quantity_input = WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("2")

        delay()

        add_to_cart = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()

        time.sleep(5)

        #add_to_cart_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, H.page_cart)))

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


def teardown(self):
    self.driver.quit()


#if __name__ == "__main__":
#    unittest.main()

