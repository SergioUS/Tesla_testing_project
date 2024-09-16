# Unittest, includes Positive and Negative tests for Tesla site, Shop Apparel and Model 3 modules(prepared by Natalia Skubii)


import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import HelpersShopApparelModel3 as H
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(1,5))

class PositiveNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()


        # Use Edge WebDriver
        #service = EdgeService(EdgeChromiumDriverManager().install())
        #self.driver = webdriver.Edge(service=service)
        #self.driver.maximize_window()


        # Use Firefox WebDriver
        #service = FirefoxService(GeckoDriverManager().install())
        #self.driver = webdriver.Firefox(service=service)
        #self.driver.maximize_window()



    # Test Case 026: Verify that Apparel page is visible in the header and link is clickable
    def test_case_026(self):
        driver = self.driver
        print("Test Case 026")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)


        #Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        # Check if the new window title contains "Apparel"
        if "Apparel" not in driver.title:
            raise Exception("Apparel - Test Case 026 failed")
        else:
            print("Apparel is available - Test Case 026 passed")

        # Test case 027: Verify that error message is issued if domain provided incorrectly
    def test_case_027(self):
        driver = self.driver

        print("Test Case 027")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        H.moving_to_new_window(driver)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        # Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        #Click on the button "Built for Any Planet Trucker Hat"
        driver.find_element(By.XPATH, H.hat_link).click()


        #Click on the button "Email me when this item is restocked"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.emailRestoked_link))).click()

        #Enter incorrect email domain
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.input_email_link)))
        email_input.send_keys("test@incorrect_domain")

        #Click on the button "Notify me"
        notify_button = driver.find_element(By.XPATH, H.notify_button)
        notify_button.click()

        # Verify that an error message or validation occurs due to the incorrect email domain
        error_message = None
        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.invalid_email_error)))

        except:
            pass

        if error_message:
            print("Error message displayed as expected - Test Case 027 passed")
        else:
            print("No error message displayed - Test Case 027 failed")
            self.fail("No error message was shown for the incorrect email domain")

        #Test Case 028: Verify that item "Men's Cybertruck Cityscape Tee" can be added to cart
    def test_case_028(self):
        driver = self.driver

        print("Test Case 028")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        H.moving_to_new_window(driver)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        # Navigate on the Apparel link and click on the Men - Tees link
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
                var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                arguments[0].dispatchEvent(event);
                """
        driver.execute_script(hover_script, apparel)
        time.sleep(6)
        tees = driver.find_element(By.XPATH, H.tees)
        action = ActionChains(driver)
        action.move_to_element(tees).click().perform()
        time.sleep(3)


        #Click on the link "Men's Cybertruck Cityscape Tee"
        driver.find_element(By.XPATH, H.partial_link).click()
        time.sleep(5)


        #Choose an available size ("S", "M", "L", "XL", "XXL")
        #driver.find_element(By.XPATH, H.size_S).click()
        driver.find_element(By.XPATH, H.size_M).click()
        #driver.find_element(By.XPATH, H.size_L).click()
        #driver.find_element(By.XPATH, H.size_XL).click()
        #driver.find_element(By.XPATH, H.size_XXL).click()

        time.sleep(5)

        #Choose quantity (1)
        quantity_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        time.sleep(5)

        add_to_cart = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        time.sleep(5)

        add_to_cart_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
             print("Add to cart page is visible - Test Case 028 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 028 failed")

    #Test Case 029 Validate the carousel "Model 3" is functional on the Order now page
    def test_case_029(self):
        driver = self.driver

        print("Test Case 029")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        #Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        #Click on the "Order" button for Model 3
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, H.order_button)))
        order_button.click()

        H.moving_to_new_window(driver)
        page_order = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.page_order)))
        page_order.click()
        WebDriverWait(driver, 5)

        # Verify Model 3 slide
        driver.find_element(By.XPATH, H.right_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.right_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.right_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.right_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.right_carousel).click()
        time.sleep(5)
        print("----Right scroll 4 times completed")

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(5)
        print("----Left scroll 4 times completed")



    def test_case_030(self):
        driver = self.driver

        print("Test Case 030")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        #Navigate on the Apparel link and click on the Onesies button
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
        arguments[0].dispatchEvent(event);
        """
        driver.execute_script(hover_script, apparel)
        time.sleep(6)
        onesies = driver.find_element(By.XPATH, H.onesie)
        action = ActionChains(driver)
        action.move_to_element(onesies).click().perform()
        time.sleep(3)

        #Click on the Scribble T Logo Onesie link
        scribble_onesie = driver.find_element(By.XPATH, H.scribble_onesie)
        scribble_onesie.click()
        WebDriverWait(driver, 5)

        # Choose the color "Gray"
        gray_color_button = driver.find_element(By.XPATH, H.gray_color)
        gray_color_button.click()
        time.sleep(3)

        # Choose size "6"
        size_6_button = driver.find_element(By.XPATH, H.size_6)
        size_6_button.click()
        time.sleep(3)

        # Choose quantity 1
        quantity_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input1)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        WebDriverWait(driver, 5)

        add_to_cart = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart1)))
        add_to_cart.click()
        WebDriverWait(driver, 5)

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart1)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
            print("Add to cart page is visible - Test Case 030 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 030 failed")


def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()