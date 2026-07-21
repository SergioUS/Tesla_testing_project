import unittest

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

class ChromePositiveTests (unittest.TestCase):

    def setUp (self):
        service = ChromeService (executable_path=ChromeDriverManager ().install ())
        self.driver = webdriver.Chrome (service=service)
        self.driver.maximize_window ()

    def test_chrome_TCP_112 (self):
        driver = self.driver
        print (
        "                                                                                                    ")
        print (
        "                                    TESLA --> ENERGY --> UTILITIES                                 ")
        print (
        "                                                                                                    ")
        print (
        "---------------------------------------- POSITIVE TEST CASES ---------------------------------------")
        print (
        "                                                                                                    ")
        print (
        "                                                                                                    ")
        print (
        "           ***  Test Case TC - 112  ***                                                             ")
        print (
        "                                                                                                    ")
        # 1. Navigate to Tesla.com
        driver.get ('https://www.tesla.com/')
        self.driver.maximize_window ()

        # 2. Click the "Energy" link in the main navigation bar
        driver.implicitly_wait (5)
        energy = driver.find_element(By.XPATH, "//span[contains(text(),'Energy')]")
        energy.click()

        # 3. Click the "Utilities" link
        driver.implicitly_wait (2)
        utilities = driver.find_element(By.LINK_TEXT, "Utilities")
        utilities.click()

        # 4. Verify that the page title matches the page content
        try:
        # Wait up to 10 seconds for the element to be present
        # presence_of_element_located returns the WebElement if found
            utilities_header = WebDriverWait (self.driver, 3).until (
            EC.presence_of_element_located ((By.XPATH, "//h1[contains(.,'Utilities')]"))
                )

            # Check for presence after waiting
            self.assertIsNotNone (utilities_header, "Utilities header element was not found after waiting.")
            print ("\nUtilities header is present on the page.")  # Newline for cleaner unittest output

        except TimeoutException:
            # If TimeoutException occurs, it means the element was not found within the timeout.
            self.fail ("Utilities header was NOT found on the page within the timeout.")
        except Exception as e:
            # Catch any other unexpected exceptions
            self.fail (f"An unexpected error occurred: {e}")

        print ("The browser correctly navigates to the Utilities page.")

        print ("Test passed: page is working as expected")
        print (
        "     ***  TC-112 - Test Case TC - 112  PASSED  ***                                              ")

    def test_chrome_TCP_113 (self):
        driver = self.driver
        print (
        "                                                                                                ")
        print (

        "           ***  Test Case TC - 113  ***                                                             ")

        # 1. Navigate to Tesla.com
        driver.get ('https://www.tesla.com/')
        self.driver.maximize_window ()

        # 2. Click the "Energy" link in the main navigation bar
        driver.implicitly_wait (3)
        energy = driver.find_element (By.XPATH, "//span[contains(text(),'Energy')]")
        energy.click ()

        # 3. Click the "Utilities" link
        driver.implicitly_wait (3)
        utilities = driver.find_element (By.LINK_TEXT, "Utilities")
        utilities.click ()


        # 4. Click on the "Contact Us" button.
        contactus = driver.find_element(By.CSS_SELECTOR, 'a[href="#contact-us"]')
        contactus.click ()




    def tearDown (self):
        self.driver.quit ()



    if __name__ == '__main__':
        unittest.main ()











# 6. Check if the main content for the "Utilities" page is displayed correctly.
