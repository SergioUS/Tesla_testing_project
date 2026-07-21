import time
import unittest
import random

from requests import options
from selenium import webdriver
from webdriver_manager.core import driver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common import WebDriverException as WDE
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def delay():
    time.sleep(random.randint(2 , 4))

class FirefoxTests(unittest.TestCase):
    def setUp(self):
        # Setup for Firefox browser
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
    def test_Fox_112(self):
        # Define a test case named `test_chrome_112`.

        driver = self.driver
        # Use the WebDriver instance created in the `setUp` method for browser interactions.

        driver.get("https://www.tesla.com/")
        # Navigate to the Tesla homepage.

        delay()
        # Introduce a random delay to wait for the page to load.
        # This approach can be improved with dynamic waits like `WebDriverWait`.

        energy_menu = driver.find_element(By.XPATH, "//button[@id='dx-nav-item--energy']")
        # Locate the "Energy" menu button using its XPath.
        # The XPath addresses an element with the `id` attribute `dx-nav-item--energy`.

        action = ActionChains(driver)
        # Create an instance of ActionChains to perform advanced user interactions.

        action.move_to_element(energy_menu).perform()
        # Simulate a hover action over the "Energy" menu item.

        driver.find_element(By.XPATH, "//a[@href='/utilities']").click()
        # Locate and click the "Utilities" submenu using its XPath.

        delay()
        # Another random delay to wait for the "Utilities" page to fully load.

        driver.find_element(By.XPATH, "//h1[contains(.,'Utilities')]")
        # Verify that the "Utilities" page has loaded by checking for an `<h1>` tag
        # containing the text "Utilities".

        if driver.current_url == "https://www.tesla.com/utilities":
            # Check if the current page URL matches the expected "Utilities" page URL.

            print("Test 112 - Passed, URL is correct")
            # Output a success message if the URL validation passes.

        else:
            print("Test 112 - Failed, URL is incorrect", driver.current_url)
            # If the URL validation fails, print a failure message along with the current URL.

        driver.quit()

    def test_Fox_113(self):
        driver = self.driver  # Assign the WebDriver instance created in the setup phase to `driver`
        # Assign the WebDriver instance initialized in the `setUp` method of the test class to the variable `driver`.
        # This allows interaction with the browser session throughout the test.

        driver.get("https://www.tesla.com/")
        # Navigate to the Tesla homepage.

        delay()
        # Introduce a delay (randomized between 2 to 4 seconds) to allow the page to load fully.
        # This should be replaced with explicit or implicit waits for better reliability.

        energy_menu = driver.find_element(By.XPATH, "//button[@id='dx-nav-item--energy']")
        # Locate the "Energy" menu button on the Tesla homepage using its XPath.
        # The XPath targets an element (`<button>`) with the `id` attribute `dx-nav-item--energy`.
        # Fails if the element is not found.

        action = ActionChains(driver)
        # Create an `ActionChains` instance to perform advanced user interactions like hovering or clicking.

        action.move_to_element(energy_menu).perform()
        # Simulate a hover action over the "Energy" menu button.

        driver.find_element(By.XPATH, "//a[@href='/utilities']").click()
        # Locate the "Utilities" submenu link using its XPath and click it.
        # This action triggers navigation to the "Utilities" page of the Tesla website.

        delay()
        # Introduce another delay to ensure the page is fully loaded.

        driver.find_element(By.XPATH, "//a[@title='Contact Us']").click()
        # Locate the "Contact Us" link on the "Utilities" page using its XPath and click it.
        # Clicking this should navigate to the Contact Us section.

        delay()
        # Introduce another delay to allow the Contact Us section of the page to load completely.

        element = driver.current_url
        # Store the current URL of the browser in the variable `element`.

        if driver.current_url == "https://www.tesla.com/utilities#contact-us" and len(element) > 0:
            # Check whether the current URL matches the expected URL for the Contact Us section.
            # Also, confirm that the `current_url` string is not empty by checking its length.

            print("Test 113 - Passed, Contact page is reached")
            # Print a success message if both conditions are met (URL is correct and non-empty).

        else:
            # If the conditions for a successful test are not met...

            print("Test 113 - Failed, Contact page is not reached")
            # Print a failure message indicating the Contact page was not reached.

        driver.quit()
        # Terminate the browser session and clean up resources regardless of test success or failure.

    def test_Fox_114(self):
        driver = self.driver
        driver.get("https://www.tesla.com/")
        time.sleep(3)

        # Navigate to "Energy" > "Utilities" menu
        energy_menu = driver.find_element(By.XPATH, "//button[@id='dx-nav-item--energy']")
        action = ActionChains(driver)
        action.move_to_element(energy_menu).perform()
        delay()

        # Click on "Utilities" submenu
        driver.find_element(By.XPATH, "//a[@href='/utilities']").click()
        time.sleep(3)

        # Scroll down to the contact form
        contact_form = driver.find_element(By.XPATH,
                                           "(//span[contains(.,'Inquire About Utility Products and Services')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", contact_form)
        time.sleep(4)

        # Fill out the contact form fields
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Max")
        # firstname.send_keys("Max")
        delay()

        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Effort")
        delay()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Max@effort.com")
        delay()
        driver.find_element(By.XPATH, "//input[@name='companyName']").send_keys("Effortless, LLC")
        delay()

        # Submit the form
        submit_form = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        driver.execute_script("arguments[0].scrollIntoView();", submit_form)
        delay()
        submit_form.click()
        delay()

        # Verify confirmation message
        confirmation_message = driver.find_element(By.XPATH, "//div[contains(@class, 'form-confirmation')]")
        self.assertTrue(
            confirmation_message.is_displayed(),
            "Confirmation message is not displayed after form submission!"
        )
        self.assertIn(
            "Thank you for contacting us", confirmation_message.text,
            "Confirmation message text did not match the expected value!"
        )
        driver.quit()

    def test_Fox_115(self):
        def test_tesla_energy_navigation(self):
            try:
                # Navigate to Tesla.com
                self.driver.get("https://www.tesla.com")

                # Hover over Energy menu
                energy_menu = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Energy']"))
                )
                ActionChains(self.driver).move_to_element(energy_menu).perform()

                # Click on Utilities option
                utilities_link = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Utilities')]"))
                )
                utilities_link.click()

                # Scroll to Manage Complexity section
                manage_complexity = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Manage Complexity')]"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView();", manage_complexity)

                # Find and click Learn More button
                learn_more_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Learn More')]"))
                )
                learn_more_button.click()

                # Verify navigation to Tesla Energy Software page
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Tesla Energy Software')]"))
                )

                # Additional verification of correct page
                assert "Tesla Energy Software" in self.driver.title, "Failed to navigate to Tesla Energy Software page"

            except Exception as e:
                raise Exception(f"Test failed: {str(e)}")

        def teardown_method(self):
            # Close the browser
            if self.driver:
                self.driver.quit()
if __name__ == '__main__':
    unittest.main()
