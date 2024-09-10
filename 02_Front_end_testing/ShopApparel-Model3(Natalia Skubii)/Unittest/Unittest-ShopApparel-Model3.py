#Natalia Skubii

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

def delay():
    time.sleep(random.randint(1,5))

class PositiveTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Test Case 026: Verify that Apparel page is visible in the header and link is clickable
    def test_case_026(self):
        driver = self.driver
        print("Test Case 026")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)  # Let the page load completely

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)  # Wait for page to load

        H.moving_to_new_window(driver)

        #Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)  # Wait for the page to load

        H.moving_to_new_window(driver)

        #Verify that the Apparel page is loaded by checking URL or page title
        self.assertIn("apparel", driver.current_url.lower(), "Apparel page not loaded")

        # Test case 027: Verify that error message is issued if domain provided incorrectly
    def test_case_027(self):
        driver = self.driver

        print("Test Case 027")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, H.shop_link))).click()

        H.moving_to_new_window(driver)


        #Click on the header menu "Apparel"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, H.apparel_link))).click()

        H.moving_to_new_window(driver)


        #Click on the button "Built for Any Planet Trucker Hat"
        driver.find_element(By.XPATH, H.hat_link).click()


        #Click on the button "Email me when this item is restocked"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, H.emailRestoked_link))).click()

        #Enter incorrect email domain
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.input_email_link)))
        email_input.send_keys("test@incorrect_domain")

        #Click on the button "Notify me"
        notify_button = driver.find_element(By.XPATH, H.notify_button)
        notify_button.click()

        #Verify that an error message is displayed (replace with actual error message locator or content)
        error_message = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.XPATH, H.invalid_email_error)))
        self.assertTrue(error_message.is_displayed(), "Error message not displayed for incorrect email domain")

        #Test Case 028: Verify that item "Men's Cybertruck Cityscape Tee" can be added to cart
    def test_case_028(self):
        driver = self.driver

        print("Test Case 028")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, H.shop_link))).click()

        H.moving_to_new_window(driver)


        #Navigate on the header menu "Apparel" and click on the link "Tees"

        apparel_url = H.apparel_url
        driver.get(apparel_url)
        WebDriverWait(driver, 10)


        menTees_url = H.menTees_url
        driver.get(menTees_url)

        H.moving_to_new_window(driver)
        WebDriverWait(driver, 10)



        #Click on the link "Men's Cybertruck Cityscape Tee"
        driver.find_element(By.XPATH, H.partial_link).click()

        H.moving_to_new_window(driver)

        #Choose the size ("S", "M", "L", "XL", "XXL")

        #driver.find_element(By.XPATH, H.size_S).click()
        driver.find_element(By.XPATH, H.size_M).click()
        #driver.find_element(By.XPATH, H.size_L).click()
        #driver.find_element(By.XPATH, H.size_XL).click()
        #driver.find_element(By.XPATH, H.size_XXL).click()

        WebDriverWait(driver, 5)

        #Choose quantity (1)
        quantity_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        WebDriverWait(driver,10)

        #Click on the button "Add to cart"

        driver.find_element(By.XPATH, H.add_to_cart).click()
        delay()


        #Validate that "Add to Cart" button has worked and cart page is displayed
        add_to_cart_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))

        self.assertTrue(add_to_cart_confirmation.is_displayed(), "Add to Cart confirmation not displayed")
        if add_to_cart_confirmation.is_displayed():
            print("Add to cart confirmation is visible - Test Case 028 passed")
        else:
            raise Exception("Add to cart confirmation is not visible - Test Case 028 failed")



if __name__ == "__main__":
    unittest.main()