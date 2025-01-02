# Unittest, includes Positive tests for Tesla site, Solar Panels module (prepared by Alexander Kulik)

import time
import unittest
import random
from webbrowser import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver import requests
from webdriver_manager.drivers.edge import EdgeChromiumDriver
#import HtmlTestRunner
import AllureReports



def delay():
    time.sleep(random.randint(1, 4))

class ChromeTests(unittest.TestCase):

    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    # POSITIVE TEST CASES

    # BR077: Verify that clicking the "Energy" button displays a dropdown menu with the "Solar Panel" option and that it works correctly.
    def test_BR077_energy_button(self):
        driver = self.driver
        # Step 1: Open Tesla Solar Panels page
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        # Step 2: Find and click the 'Energy' button
        print("Step 2: Find and click the 'Energy' button.")
        try:
            driver.find_element(By.XPATH, "//h2[contains(text(),'Energy')]").click()
            print("'Energy' button clicked successfully.")
        except:
            print("Could not find or click the 'Energy' button.")
            return

        delay()

        # Step 3: Verify dropdown menu appears with 'Solar Panels' option
        print("Step 3: Verify dropdown menu appears with 'Solar Panels' option.")
        try:
            driver.find_element(By.XPATH, "//a[text()='Solar Panels']").click()
            print("'Solar Panels' option clicked successfully.")
        except:
            print("Could not find or click the 'Solar Panels' option.")
            return

        delay()

        # Step 4: Verify navigation to Solar Panels page
        print("Step 4: Verify navigation to Solar Panels page.")
        if "solarpanels" in driver.current_url:
            print("Successfully navigated to the Solar Panels page.")
        else:
            print("Failed to navigate to the Solar Panels page.")

    # BR078: Check that clicking the 'Order Now' button takes the user to the solar panel order form.
    def test_BR078_order_now_button(self):
        driver = self.driver
        # Step 1: Open Tesla Solar Panels page
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        # Step 2: Find and click the 'Order Now' button
        print("Step 2: Find and click the 'Order Now' button.")
        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").click()
            print("'Order Now' button clicked successfully.")
        except:
            print("Could not find or click the 'Order Now' button.")
            return

        delay()

        # Step 3: Verify navigation to the order form
        print("Step 3: Verify navigation to the order form.")
        try:
            driver.find_element(By.XPATH, "//div[contains(@class,'OyqQf')]").click()
            print("Successfully navigated to the order form page.")
        except:
            print("Test 078 fail. Failed to navigate to the order form. Current URL: {driver.current_url}")
            return

        # Step 4: Check input fields visibility
        print("Step 4: Check input fields visibility.")
        input_fields = driver.find_elements(By.XPATH, "//input")
        if all(field.is_displayed() for field in input_fields):
            print("All input fields are displayed correctly.")
        else:
            print("Some input fields are not visible.")

    # BR079: Verify that the "Schedule Consultation" button allows users to book a consultation.
    def test_BR079_schedule_consultation_button(self):
        driver = self.driver
        # Step 1: Open Tesla Solar Panels page
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        # Step 2: Click on the 'Schedule Consultation' button
        print("Step 2: Click on the 'Schedule Consultation' button.")
        try:
            driver.find_element(By.XPATH, "(//a[contains(.,'Schedule a Consultation')])[2]").click()
            print("'Schedule Consultation' button clicked successfully.")
        except:
            print("Could not find or click the 'Schedule Consultation' button.")
            return

        delay()

        # Step 3: Verify consultation form appears
        print("Step 3: Verify consultation form appears.")
        try:
            form = driver.find_element(By.XPATH, "//form")
            if form.is_displayed():
                print("Consultation form is visible.")
            else:
                print("Consultation form is not visible.")
        except:
            print("Consultation form not found.")

    # BR080: Verify that languages button is clickable and client can change languages (English, Spanish, French).
    def test_BR080_languages_button(self):
        driver = self.driver
        # Step 1: Open Tesla Solar Panels page
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        # Step 2: Find and click the 'Languages' button
        print("Step 2: Find and click the 'Languages' button.")
        try:
            driver.find_element(By.XPATH, "//button[@id='dx-nav-item--locale-selector']").click()
            print("'Languages' button clicked successfully.")
        except:
            print("Could not find or click the 'Languages' button.")
            return

        delay()

        # Step 3: Select Spanish language
        print("Step 3: Select Spanish language.")
        try:
            driver.find_element(By.XPATH, "//a[contains(text(), 'Español')]").click()
            print("Switched to Spanish language successfully.")
        except:
            print("Could not switch to Spanish language.")
            return

    # BR081: Verify that the on Solar Panels page button "Chat" is clickable.
    def test_BR081_chat_button(self):
        driver = self.driver
        # Step 1: Open Tesla Solar Panels page
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        # Step 2: Find and click the 'Chat' button
        print("Step 2: Find and click the 'Chat' button.")
        try:
            driver.find_element(By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']").click()
            print("'Chat' button clicked successfully.")
        except:
            print("Could not find or click the 'Chat' button.")
            return

        delay()

        # Step 3: Verify chat window visibility
        print("Step 3: Verify chat window visibility.")
        try:
            chat_window = driver.find_element(By.XPATH, "(//div[contains(@class,'tw-chat--tds-form-label')])[1]")
            if chat_window.is_displayed():
                print("Chat window opened successfully.")
            else:
                print("Chat window did not open.")
        except:
            print("Chat window not found.")

    def tearDown(self):
        print("Closing the browser.")
        self.driver.quit()

        # NEGATIVE TEST CASES

        # BR077: Verify error message when accessing the Solar Panels page with a broken link.
    def test_TC077_broken_link(self):
        driver = self.driver
        print("Step 1: Navigate to a broken URL.")
        driver.get("https://www.tesla.com/solarpanel.")  # Broken URL
        delay()

        print("Step 2: Verify that a 404 error message is displayed.")
        try:
            error_message = driver.find_element(By.XPATH, "//h1[contains(text(),'404')]")
            self.assertTrue(error_message.is_displayed(), "Error message is not displayed.")
            print("Result: 404 error message displayed as expected.")
        except NoSuchElementException:
            print("Result: 404 error message not found.")
        finally:
            delay()

        # BR078: Verify that clicking the 'Order Now' button without entering the required address prevents proceeding.
    def test_BR078_order_now_no_address(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Click the 'Order Now' button.")
        try:
            order_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Order Now')])[1]"))
            )
            order_now_button.click()
            print("Result: 'Order Now' button clicked successfully.")
        except NoSuchElementException:
            print("Result: 'Order Now' button not found.")

        delay()

        print("Step 3: Verify 'Next' button is disabled without entering an address.")
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
            self.assertFalse(next_button.is_enabled(), "Result: 'Next' button is enabled without address.")
            print("Result: 'Next' button is correctly disabled without address.")
        except NoSuchElementException:
            print("Result: 'Next' button not found.")
        finally:
            delay()

        # BR079: Verify that the user cannot enter a value below $20 in the 'Average Electric Bill' field.
    def test_BR079_average_bill_min_value(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a value less than $20 in the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("19")
            print("Result: Value 19 entered.")

            print("Step 3: Verify error message is displayed.")
            error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]")
            self.assertTrue(error_message.is_displayed(), "Error message not displayed for value below $20.")
            print("Result: Error message displayed correctly.")
        except NoSuchElementException:
            print("Result: Field or error message not found.")
        finally:
            delay()

        # BR080: Verify that user cannot add letters to 'Average Electric Bill' field.
    def test_BR080_no_letters_in_bill_field(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter letters into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("abc")
            print("Result: Letters 'abc' entered.")

            print("Step 3: Verify that letters are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted letters.")
            print("Result: Letters were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

        # BR081: Verify that user cannot add negative integers to the 'Average Electric Bill' field.
    def test_BR081_no_negative_integers(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a negative integer into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("-5")
            print("Result: Negative value '-5' entered.")

            print("Step 3: Verify that negative values are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted negative value.")
            print("Result: Negative values were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

    def tearDown(self):
        print("Closing the browser.")
        self.driver.quit()






class FirefoxTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    # POSITIVE TEST CASES

    # BR077: Verify that clicking the "Energy" button displays a dropdown menu with the "Solar Panel" option and that it works correctly.
    def test_BR077_energy_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Energy' button.")
        try:
            energy_button = driver.find_element(By.XPATH, "//h2[contains(text(),'Energy')]")
            energy_button.click()
            print("'Energy' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Energy' button.")
            return

        delay()

        print("Step 3: Verify dropdown menu appears with 'Solar Panels' option.")
        try:
            solar_panels_option = driver.find_element(By.XPATH, "//a[text()='Solar Panels']")
            solar_panels_option.click()
            print("'Solar Panels' option clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Solar Panels' option.")
            return

        delay()

        print("Step 4: Verify navigation to Solar Panels page.")
        self.assertIn("solarpanels", driver.current_url, "Failed to navigate to the Solar Panels page.")
        print("Successfully navigated to the Solar Panels page.")

    # BR078: Check that clicking the 'Order Now' button takes the user to the solar panel order form.
    def test_BR078_order_now_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Order Now' button.")
        try:
            order_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Order Now')])[1]"))
            )
            order_now_button.click()
            print("'Order Now' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Order Now' button.")
            return

        delay()

        print("Step 3: Verify navigation to the order form.")
        self.assertIn("design", driver.current_url, "Failed to navigate to the order form.")
        print("Successfully navigated to the order form page.")

    # BR079: Verify that the "Schedule Consultation" button allows users to book a consultation.
    def test_BR079_schedule_consultation_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Click on the 'Schedule Consultation' button.")
        try:
            schedule_button = driver.find_element(By.XPATH, "(//a[contains(.,'Schedule a Consultation')])[2]")
            schedule_button.click()
            print("'Schedule Consultation' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Schedule Consultation' button.")
            return

        delay()

        print("Step 3: Verify consultation form appears.")
        try:
            form = driver.find_element(By.XPATH, "//form")
            self.assertTrue(form.is_displayed(), "Consultation form is not visible.")
            print("Consultation form is visible.")
        except NoSuchElementException:
            print("Consultation form not found.")

    # BR080: Verify that languages button is clickable and client can change languages (English, Spanish, French).
    def test_BR080_languages_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Languages' button.")
        try:
            language_button = driver.find_element(By.XPATH, "//button[@id='dx-nav-item--locale-selector']")
            language_button.click()
            print("'Languages' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Languages' button.")
            return

        delay()

        print("Step 3: Select Spanish language.")
        try:
            spanish_option = driver.find_element(By.XPATH, "//a[contains(text(), 'Español')]")
            spanish_option.click()
            print("Switched to Spanish language successfully.")
        except NoSuchElementException:
            print("Could not switch to Spanish language.")
            return

    # BR081: Verify that the on Solar Panels page button "Chat" is clickable.
    def test_BR081_chat_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Chat' button.")
        try:
            chat_button = driver.find_element(By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")
            chat_button.click()
            print("'Chat' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Chat' button.")
            return

        delay()

        print("Step 3: Verify chat window visibility.")
        try:
            chat_window = driver.find_element(By.XPATH, "(//div[contains(@class,'tw-chat--tds-form-label')])[1]")
            self.assertTrue(chat_window.is_displayed(), "Chat window did not open.")
            print("Chat window opened successfully.")
        except NoSuchElementException:
            print("Chat window not found.")

    # NEGATIVE TEST CASES

    # BR077: Verify error message when accessing the Solar Panels page with a broken link.
    def test_TC006_broken_link(self):
        driver = self.driver
        print("Step 1: Navigate to a broken URL.")
        driver.get("https://www.tesla.com/solarpanel.")  # Broken URL
        delay()

        print("Step 2: Verify that a 404 error message is displayed.")
        try:
            error_message = driver.find_element(By.XPATH, "//h1[contains(text(),'404')]")
            self.assertTrue(error_message.is_displayed(), "Error message is not displayed.")
            print("Result: 404 error message displayed as expected.")
        except NoSuchElementException:
            print("Result: 404 error message not found.")
        finally:
            delay()

    # BR078: Verify that clicking the 'Order Now' button without entering the required address prevents proceeding.
    def test_BR078_order_now_no_address(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Click the 'Order Now' button.")
        try:
            order_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Order Now')])[1]"))
            )
            order_now_button.click()
            print("Result: 'Order Now' button clicked successfully.")
        except NoSuchElementException:
            print("Result: 'Order Now' button not found.")
            return
        delay()

        print("Step 3: Verify 'Next' button is disabled without entering an address.")
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
            self.assertFalse(next_button.is_enabled(), "Result: 'Next' button is enabled without address.")
            print("Result: 'Next' button is correctly disabled without address.")
        except NoSuchElementException:
            print("Result: 'Next' button not found.")
        finally:
            delay()

    # BR079: Verify that the user cannot enter a value below $20 in the 'Average Electric Bill' field.
    def test_BR079_average_bill_min_value(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a value less than $20 in the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("19")
            print("Result: Value 19 entered.")

            print("Step 3: Verify error message is displayed.")
            error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]")
            self.assertTrue(error_message.is_displayed(), "Error message not displayed for value below $20.")
            print("Result: Error message displayed correctly.")
        except NoSuchElementException:
            print("Result: Field or error message not found.")
        finally:
            delay()

    # BR080: Verify that user cannot add letters to 'Average Electric Bill' field.
    def test_BR080_no_letters_in_bill_field(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter letters into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("abc")
            print("Result: Letters 'abc' entered.")

            print("Step 3: Verify that letters are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted letters.")
            print("Result: Letters were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

    # BR081: Verify that user cannot add negative integers to the 'Average Electric Bill' field.
    def test_BR081_no_negative_integers(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a negative integer into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("-5")
            print("Result: Negative value '-5' entered.")

            print("Step 3: Verify that negative values are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted negative value.")
            print("Result: Negative values were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

    def tearDown(self):
        print("Closing the browser.")
        self.driver.quit()




def delay():
    time.sleep(random.randint(1, 4))

class EdgeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

    # POSITIVE TEST CASES

    # BR077: Verify that clicking the "Energy" button displays a dropdown menu with the "Solar Panel" option and that it works correctly.
    def test_BR077_energy_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Energy' button.")
        try:
            energy_button = driver.find_element(By.XPATH, "//h2[contains(text(),'Energy')]")
            energy_button.click()
            print("'Energy' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Energy' button.")
            return

        delay()

        print("Step 3: Verify dropdown menu appears with 'Solar Panels' option.")
        try:
            solar_panels_option = driver.find_element(By.XPATH, "//a[text()='Solar Panels']")
            solar_panels_option.click()
            print("'Solar Panels' option clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Solar Panels' option.")
            return

        delay()

        print("Step 4: Verify navigation to Solar Panels page.")
        self.assertIn("solarpanels", driver.current_url, "Failed to navigate to the Solar Panels page.")
        print("Successfully navigated to the Solar Panels page.")

    # BR078: Check that clicking the 'Order Now' button takes the user to the solar panel order form.
    def test_BR078_order_now_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Order Now' button.")
        try:
            order_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Order Now')])[1]"))
            )
            order_now_button.click()
            print("'Order Now' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Order Now' button.")
            return

        delay()

        print("Step 3: Verify navigation to the order form.")
        self.assertIn("design", driver.current_url, "Failed to navigate to the order form.")
        print("Successfully navigated to the order form page.")

    # BR079: Verify that the "Schedule Consultation" button allows users to book a consultation.
    def test_BR079_schedule_consultation_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Click on the 'Schedule Consultation' button.")
        try:
            schedule_button = driver.find_element(By.XPATH, "(//a[contains(.,'Schedule a Consultation')])[2]")
            schedule_button.click()
            print("'Schedule Consultation' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Schedule Consultation' button.")
            return

        delay()

        print("Step 3: Verify consultation form appears.")
        try:
            form = driver.find_element(By.XPATH, "//form")
            self.assertTrue(form.is_displayed(), "Consultation form is not visible.")
            print("Consultation form is visible.")
        except NoSuchElementException:
            print("Consultation form not found.")

    # BR080: Verify that languages button is clickable and client can change languages (English, Spanish, French).
    def test_BR080_languages_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Languages' button.")
        try:
            language_button = driver.find_element(By.XPATH, "//button[@id='dx-nav-item--locale-selector']")
            language_button.click()
            print("'Languages' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Languages' button.")
            return

        delay()

        print("Step 3: Select Spanish language.")
        try:
            spanish_option = driver.find_element(By.XPATH, "//a[contains(text(), 'Español')]")
            spanish_option.click()
            print("Switched to Spanish language successfully.")
        except NoSuchElementException:
            print("Could not switch to Spanish language.")
            return

    # BR081: Verify that the on Solar Panels page button "Chat" is clickable.
    def test_BR081_chat_button(self):
        driver = self.driver
        print("Step 1: Open Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Find and click the 'Chat' button.")
        try:
            chat_button = driver.find_element(By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")
            chat_button.click()
            print("'Chat' button clicked successfully.")
        except NoSuchElementException:
            print("Could not find or click the 'Chat' button.")
            return

        delay()

        print("Step 3: Verify chat window visibility.")
        try:
            chat_window = driver.find_element(By.XPATH, "(//div[contains(@class,'tw-chat--tds-form-label')])[1]")
            self.assertTrue(chat_window.is_displayed(), "Chat window did not open.")
            print("Chat window opened successfully.")
        except NoSuchElementException:
            print("Chat window not found.")

    # NEGATIVE TEST CASES

    # BR077: Verify error message when accessing the Solar Panels page with a broken link.
    def test_BR077_broken_link(self):
        driver = self.driver
        print("Step 1: Navigate to a broken URL.")
        driver.get("https://www.tesla.com/solarpanel.")  # Broken URL
        delay()

        print("Step 2: Verify that a 404 error message is displayed.")
        try:
            error_message = driver.find_element(By.XPATH, "//h1[contains(text(),'404')]")
            self.assertTrue(error_message.is_displayed(), "Error message is not displayed.")
            print("Result: 404 error message displayed as expected.")
        except NoSuchElementException:
            print("Result: 404 error message not found.")
        finally:
            delay()

    # BR078: Verify that clicking the 'Order Now' button without entering the required address prevents proceeding.
    def test_BR078_order_now_no_address(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Click the 'Order Now' button.")
        try:
            order_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Order Now')])[1]"))
            )
            order_now_button.click()
            print("Result: 'Order Now' button clicked successfully.")
        except NoSuchElementException:
            print("Result: 'Order Now' button not found.")
            return
        delay()

        print("Step 3: Verify 'Next' button is disabled without entering an address.")
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
            self.assertFalse(next_button.is_enabled(), "Result: 'Next' button is enabled without address.")
            print("Result: 'Next' button is correctly disabled without address.")
        except NoSuchElementException:
            print("Result: 'Next' button not found.")
        finally:
            delay()

    # BR079: Verify that the user cannot enter a value below $20 in the 'Average Electric Bill' field.
    def test_BR079_average_bill_min_value(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a value less than $20 in the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("19")
            print("Result: Value 19 entered.")

            print("Step 3: Verify error message is displayed.")
            error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]")
            self.assertTrue(error_message.is_displayed(), "Error message not displayed for value below $20.")
            print("Result: Error message displayed correctly.")
        except NoSuchElementException:
            print("Result: Field or error message not found.")
        finally:
            delay()

    # BR080: Verify that user cannot add letters to 'Average Electric Bill' field.
    def test_BR080_no_letters_in_bill_field(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter letters into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("abc")
            print("Result: Letters 'abc' entered.")

            print("Step 3: Verify that letters are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted letters.")
            print("Result: Letters were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

    # BR081: Verify that user cannot add negative integers to the 'Average Electric Bill' field.
    def test_BR081_no_negative_integers(self):
        driver = self.driver
        print("Step 1: Open the Tesla Solar Panels page.")
        driver.get("https://www.tesla.com/solarpanels")
        delay()

        print("Step 2: Enter a negative integer into the 'Average Electric Bill' field.")
        try:
            bill_field = driver.find_element(By.XPATH, "//input[@name='electric-bill']")
            bill_field.send_keys("-5")
            print("Result: Negative value '-5' entered.")

            print("Step 3: Verify that negative values are blocked.")
            self.assertEqual(bill_field.get_attribute("value"), "", "Field accepted negative value.")
            print("Result: Negative values were correctly blocked.")
        except NoSuchElementException:
            print("Result: Field not found.")
        finally:
            delay()

    def tearDown(self):
        print("Closing the browser.")
        self.driver.quit()

#if __name__ == "__main__":
    #unittest.main()

#if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

if __name__ == "__main__":
    unittest.main(AllureReports)

