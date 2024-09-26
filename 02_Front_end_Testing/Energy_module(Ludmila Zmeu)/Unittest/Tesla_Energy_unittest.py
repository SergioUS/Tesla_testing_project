  # Unittest, includes Positive and Negative tests for Tesla site, Energy module(prepared by Ludmila Zmeu)

import random
import time
import unittest
import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
fake = faker.Faker()


def delay():


   time.sleep(random.randint(1, 5))


class ChromePositiveTestCases(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome(service=ChromeService())
       self.driver.maximize_window()


     # Test case 021 positive. Verify that "Energy" button is clickable and transfer to correct page.

   def test_case_021_positive_energy_page(self):
       driver = self.driver

       print("Test Case 021")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")
       driver.maximize_window()

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       print("Energy is available- Test case 021 passed")


     # Test case 022 positive. Validate that "Solar Roof" element is visible in the header and  is clickable

   def test_case022_positive_solar_roof_button(self):
       driver = self.driver

       print("Test Case 022")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(4)

       # 3. Click "Solar Roof" element on the menu page
       solar_roof_button = driver.find_element(By.XPATH, "//img[@alt ='Solar Roof']")
       solar_roof_button.click()
       delay()

       # 4.Check if the new window contains title "Solar Roof"
       self.assertIn("Solar Roof", driver.title)
       print("SolarRoof is available- Test case 022 passed")


   # Test Case 023 positive.  Navigate to Megapack and test "Order Now" button

   def test_case023_positive_megapack_order_page(self):
       driver = self.driver

       print("Test Case 023")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the "Energy" button on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(5)

       # 3. Click "Megapack" element on the menu page
       megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
       megapack_button.click()
       delay()

       # 4. Check if the new window contains title "Megapack"
       self.assertIn("Megapack", driver.title)

       # 5. Click on the "Order Now" button
       order_now_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="tesla-hero-5114"]/div[2]/div/section/div')))
       order_now_button.click()
       delay()

       # 6. Verify that the "Order Now" is functional and page has loaded successfully
       self.assertIn("Order Megapack", driver.title)
       print("Order Megapack is available-Test case 023 passed")


   # Test Case 024 positive.  Navigate to Megapack page and test "Video" on the page

   def test_case024_positive_megapack_video_page(self):
       driver = self.driver

       print("Test Case 024")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the "Energy" button on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Click "Megapack" element on the menu page
       megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
       megapack_button.click()
       delay()

       # 4. Check if the new window contains title "Megapack"
       self.assertIn("Megapack", driver.title)

       # 5. Find the first video on the page "Megapack"
       driver.execute_script("window.scrollTo(0,2800)")
       time.sleep(5)
       video = driver.find_element(By.XPATH,
                         '//*[@id="tesla-text-with-media-137"]/section/section[1]/div/div/video')
       driver.save_screenshot("video1.png")
       video.click()
       time.sleep(6)
       driver.save_screenshot("video2.png")
       print("video is playing.Check Screenshots.- Test Case 024 passed")


     # Test Case 025 positive. Navigate to "Powerwall" page and Validate that page have access to translator page
     # in "Romana"

   def test_case025_positive_powerwall_page_română(self):
       driver = self.driver

       print("Test Case 025")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Click on the " Powerwall" element
       powerwall_button = WebDriverWait(driver, 5).until(
          EC.element_to_be_clickable((By.XPATH, "//img[@alt='Powerwall']")))
       powerwall_button.click()
       time.sleep(2)

       # 4. Check if the new window contains title "Powerwall"
       self.assertIn("Powerwall", driver.title)
       time.sleep(3)

       # 5.Click on "globe" button
       globe_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='dx-nav-item--locale-selector']")))
       globe_button.click()
       time.sleep(2)

       # 6. Select "Română" language
       română_language_button = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Română')]")))
       română_language_button.click()
       time.sleep(3)

       # 7. Verify if the page is in "Română"by checking the page title or specific content
       error_message = driver.find_element(By.XPATH, "//h1[@class='error-code'][contains(.,'404')]")
       if 404 and error_message:
           print("Test case 025 fail")
       else:
           print("Test case 025 passed")


     # Test Case 021 negative.  Validate that in the "Solar Panels" page is possible to access  "Order Now " button and
     # can't click "Next" without provide any user information

   def test_case021_negative_solar_panels_order_now_page(self):
       driver = self.driver

       print("Test Case 021 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4. Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Click on the "Order Now" button
       order_now_button = WebDriverWait(self.driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[1]")))
       order_now_button.click()
       time.sleep(3)

       # 4. Check if the new window contains title "Design your Solar"
       self.assertIn("Design your Solar", driver.title)
       time.sleep(3)

       # 6. Scroll down to find and click "Next" button without including any information
       driver.execute_script("window.scrollTo(0,1600)")
       time.sleep(5)

       # 7. Try to click "Next" without entering any user information
       next_button = driver.find_element (By.XPATH, '//*[@id="landing-page-next-btn"]')
       next_button.click()
       time.sleep(3)

       # 8. Verify that the "Next" button doesn't allow navigation without user input
       is_disabled = next_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is displayed.Test Case 021 passed")
       else:
           print("Button is not displayed. Test Case 021 negative failed")


     # Test Case 022 negative. Validate that in the "Solar Panels" page is possible to access  "Chat " button and
     # can't request a Call Back without provide any user information

   def test_case022_negative_solar_panels_chat_request_callback(self):
       driver = self.driver

       print("Test Case 022 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Scroll down to find the "Request a Callback" button
       chat_box = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]')
       actions = ActionChains(driver)
       actions.move_to_element(chat_box).click().send_keys(Keys.PAGE_DOWN).perform()
       time.sleep(5)

       # 8. Click "Request A Callback" button without including any user information
       callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
       is_disabled = callback_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is disable. Test case 022 passed")
       else:
           print("Button is not disable. Test case 022 failed")    # Pass


     #Test Case 023 negative.Validate that in the "Solar Panels " page the user enter wrong elements in Last and
     #  First Name box and can't  do the order

   def test_case023_negative_solar_panels_chat_request_callback_invalid_name(self):
       driver = self.driver

       print("Test Case 023 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Verify that the chat window is opened by checking for some chat-specific element
       WebDriverWait(driver, 5).until(
           EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
       time.sleep(2)

       # 8. Fill in the required information field with invalid name
       first_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
       first_name_input.send_keys("345565@#$%hijkj")
       time.sleep(2)

       last_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
       last_name_input.send_keys("tyuuhi^&^$#!@123")
       time.sleep(2)

       email_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
       email_input.send_keys("jepapad460@esterace.com")
       time.sleep(2)

       phone_number_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
       phone_number_input.send_keys("15674852769")
       time.sleep(2)

       zip_code_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
       zip_code_input.send_keys("78965")
       time.sleep(3)

       product_interest_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
       product_interest_input.send_keys("Solar Panels")
       time.sleep(2)

       # 9. Click "Request A Callback" button
       request_callback_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Request a Callback')]")))
       request_callback_button.click()
       time.sleep(3)

       # 10. Verify that the page is not allowed to go next
       confirmation_message = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]/div/div[1]').text
       print(confirmation_message)
       if "Thank you!" in confirmation_message:
           print(" Thank you! We will contact your soon- Test case 023 failed")
       else:
           print("Confirmation message is not present.  Test Case 023 passed")


      # Test case 024 negative. Validate that in the "Solar Panels" page the user can't send to "Request A Callback"
      # without email address

   def test_case024_negative_solar_panels_chat_request_callback_no_email(self,):
       driver = self.driver

       print("Test Case 024 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Verify that the chat window is opened by checking for some chat-specific element
       WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
       time.sleep(2)

       # 8. Fill in the required information field with invalid name
       first_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
       first_name_input.send_keys(" Ella")
       time.sleep(2)

       last_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
       last_name_input.send_keys(" Smith")
       time.sleep(2)

       phone_number_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
       phone_number_input.send_keys("15674852769")
       time.sleep(2)

       zip_code_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
       zip_code_input.send_keys("78965")
       time.sleep(3)

       product_interest_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
       product_interest_input.send_keys("Solar Panels")
       time.sleep(3)

       # 9. Click "Request A Callback" button without including user email address information
       callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
       is_disabled = callback_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is disable without email address information. Test case 024 passed")
       else:
           print("Button is not disable. Test case 024 failed")


     #Test case 025 negative. Validate if the "Support" button is clickable on the "Solar Panels page is not accessible
     # if introducing wrong data in "Support Search" line

   def test_case025_solar_panels_support_search(self):
       driver = self.driver

       print("Test Case 025 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       #  Scroll down to find the "Support" button on the header menu
       driver.execute_script("window.scrollTo(0, 1500)")
       time.sleep(3)

       # 6. Click on the "Support" button
       support_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//span[@class='tds-text--700'][contains(.,'Support')]")))
       support_button.click()
       time.sleep(2)

       # 7. Check if the new window contains title "Support"
       self.assertIn("Support", driver.title)

       # 8. Type "ncjifehhrehfl" in the "Support Search" section
       support_search_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='support-search-input']")))
       support_search_input.send_keys("ncjifehhrehfl")
       time.sleep(5)

       # 9. Click "Enter" button
       support_search_input.send_keys(Keys.ENTER)
       time.sleep(3)

       # 10. Verify that the elements provided in search page are not present
       results = driver.find_element(By.XPATH, '//*[@id="results-container"]/div/h2')
       if results:
           print("No search results with keyword fjhghhjhg- Test Case 025 passed")
       else:
           print("Results with keyword fjhghhjhg are available- Test Case 025 failed ")


class FirefoxPositiveTestCases(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
       self.driver.maximize_window()

       # Test case 021 positive. Verify that "Energy" button is clickable and transfer to correct page.

   def test_case_021_positive_energy_page(self):
       driver = self.driver

       print("Test Case 021")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")
       driver.maximize_window()

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       print("Energy is available- Test case 021 passed")


       # Test case 022 positive.  Validate that "Solar Roof" element is visible in the header and  is clickable

   def test_case022_positive_solar_roof_button(self):
       driver = self.driver

       print("Test Case 022")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(4)

       # 3. Click "Solar Roof" element on the menu page
       solar_roof_button = driver.find_element(By.XPATH, "//img[@alt ='Solar Roof']")
       solar_roof_button.click()
       delay()

       # 4.Check if the new window contains title "Solar Roof"
       self.assertIn("Solar Roof", driver.title)
       print("SolarRoof is available- Test case 022 passed")


       # Test Case 023 positive. Navigate to Megapack and test "Order Now" button

   def test_case023_positive_megapack_order_page(self):
       driver = self.driver

       print("Test Case 023")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the "Energy" button on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(5)

       # 3. Click "Megapack" element on the menu page
       megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
       megapack_button.click()
       delay()

       # 4. Check if the new window contains title "Megapack"
       self.assertIn("Megapack", driver.title)

       # 5. Click on the "Order Now" button
       order_now_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="tesla-hero-5114"]/div[2]/div/section/div')))
       order_now_button.click()
       delay()

       # 6. Verify that the "Order Now" is functional and page has loaded successfully
       self.assertIn("Order Megapack", driver.title)
       print("Order Megapack is available-Test case 023 passed")


       # Test Case 024 positive. Navigate to Megapack page and test "Video" on the page

   def test_case024_positive_megapack_video_page(self):
       driver = self.driver

       print("Test Case 024")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the "Energy" button on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Click "Megapack" element on the menu page
       megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
       megapack_button.click()
       delay()

       # 4. Check if the new window contains title "Megapack"
       self.assertIn("Megapack", driver.title)

       # 5. Find the first video on the page "Megapack"
       driver.execute_script("window.scrollTo(0,2800)")
       time.sleep(5)
       video = driver.find_element(By.XPATH,
                                   '//*[@id="tesla-text-with-media-137"]/section/section[1]/div/div/video')
       driver.save_screenshot("video1.png")
       video.click()
       time.sleep(6)
       driver.save_screenshot("video2.png")
       print("video is playing.Check Screenshots.- Test Case 024 passed")


       # Test Case 025 positive. Navigate to "Powerwall" page and Validate that page have access to translator page
       # in "Romana"

   def test_case025_positive_powerwall_page_română(self):
       driver = self.driver

       print("Test Case 025")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Click on the " Powerwall" element
       powerwall_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[@alt='Powerwall']")))
       powerwall_button.click()
       time.sleep(2)

       # 4. Check if the new window contains title "Powerwall"
       self.assertIn("Powerwall", driver.title)
       time.sleep(3)

       # 5.Click on "globe" button
       globe_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='dx-nav-item--locale-selector']")))
       globe_button.click()
       time.sleep(2)

       # 6. Select "Română" language
       română_language_button = WebDriverWait(self.driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Română')]")))
       română_language_button.click()
       time.sleep(3)

       # 7. Verify if the page is in "Română"by checking the page title or specific content
       error_message = driver.find_element(By.XPATH, "//h1[@class='error-code'][contains(.,'404')]")
       if 404 and error_message:
           print("Test case 025 fail")
       else:
           print("Test case 025 passed")


       # Test Case 021 negative. Validate that in the "Solar Panels" page is possible to access  "Order Now " button and
       # can't click "Next" without provide any user information

   def test_case021_negative_solar_panels_order_now_page(self):
       driver = self.driver

       print("Test Case 021 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4. Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Click on the "Order Now" button
       order_now_button = WebDriverWait(self.driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[1]")))
       order_now_button.click()
       time.sleep(3)

       # 4. Check if the new window contains title "Design your Solar"
       self.assertIn("Design your Solar", driver.title)
       time.sleep(3)

       # 6. Scroll down to find and click "Next" button without including any information
       driver.execute_script("window.scrollTo(0,1600)")
       time.sleep(5)

       # 7. Try to click "Next" without entering any user information
       next_button = driver.find_element(By.XPATH, '//*[@id="landing-page-next-btn"]')
       next_button.click()
       time.sleep(3)

       # 8. Verify that the "Next" button doesn't allow navigation without user input
       is_disabled = next_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is displayed.Test Case 021 passed")
       else:
           print("Button is not displayed. Test Case 021 negative failed")  # Passed


       # Test Case 022 negative. Validate that in the "Solar Panels" page is possible to access  "Chat " button and
       # can't request a Call Back without provide any user information

   def test_case022_negative_solar_panels_chat_request_callback(self):
       driver = self.driver

       print("Test Case 022 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Scroll down to find the "Request a Callback" button
       chat_box = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]')
       actions = ActionChains(driver)
       actions.move_to_element(chat_box).click().send_keys(Keys.PAGE_DOWN).perform()
       time.sleep(5)

       # 8. Click "Request A Callback" button without including any user information
       callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
       is_disabled = callback_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is disable. Test case 022 passed")
       else:
           print("Button is not disable. Test case 022 failed")  # Pass


       # Test Case 023 negative. Validate that in the "Solar Panels " page the user enter wrong elements in  Last and
       # First Name box and can't  do the order

   def test_case023_negative_solar_panels_chat_request_callback_invalid_name(self):
       driver = self.driver

       print("Test Case 023 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Verify that the chat window is opened by checking for some chat-specific element
       WebDriverWait(driver, 5).until(
           EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
       time.sleep(2)

       # 8. Fill in the required information field with invalid name
       first_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
       first_name_input.send_keys("345565@#$%hijkj")
       time.sleep(2)

       last_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
       last_name_input.send_keys("tyuuhi^&^$#!@123")
       time.sleep(2)

       email_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
       email_input.send_keys("jepapad460@esterace.com")
       time.sleep(2)

       phone_number_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
       phone_number_input.send_keys("15674852769")
       time.sleep(2)

       zip_code_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
       zip_code_input.send_keys("78965")
       time.sleep(3)

       product_interest_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
       product_interest_input.send_keys("Solar Panels")
       time.sleep(2)

       # 9. Click "Request A Callback" button
       request_callback_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Request a Callback')]")))
       request_callback_button.click()
       time.sleep(3)

       # 10. Verify that the page is not allowed to go next
       confirmation_message = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]/div/div[1]').text
       print(confirmation_message)
       if "Thank you!" in confirmation_message:
           print(" Thank you! We will contact your soon- Test case 023 failed")
       else:
           print("Confirmation message is not present.  Test Case 023 passed")  # (Failed)


       # Test case 024 negative. Validate that in the "Solar Panels" page the user can't send to "Request A Callback"
       # without email address

   def test_case024_negative_solar_panels_chat_request_callback_no_email(self, ):
       driver = self.driver

       print("Test Case 024 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       # 6. Click on the "Chat" button
       chat_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
       chat_button.click()
       time.sleep(3)

       # 7. Verify that the chat window is opened by checking for some chat-specific element
       WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
       time.sleep(2)

       # 8. Fill in the required information field with invalid name
       first_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
       first_name_input.send_keys(" Ella")
       time.sleep(2)

       last_name_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
       last_name_input.send_keys(" Smith")
       time.sleep(2)

       phone_number_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
       phone_number_input.send_keys("15674852769")
       time.sleep(2)

       zip_code_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
       zip_code_input.send_keys("78965")
       time.sleep(3)

       product_interest_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
       product_interest_input.send_keys("Solar Panels")
       time.sleep(3)

       # 9. Click "Request A Callback" button without including user email address information
       callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
       is_disabled = callback_button.get_attribute('disabled') is not None
       print(is_disabled)
       if is_disabled:
           print("Button is disable without email address information. Test case 024 passed")
       else:
           print("Button is not disable. Test case 024 failed")  # Pass


       # Test Case 025 Negative.Validate if the "Support" button is clickable on the "Solar Panels page is not
       # accessible if introducing wrong data in "Support Search" line

   def test_case025_negative_solar_panels_support_search(self):
       driver = self.driver

       print("Test Case 025 Negative")

       # 1. Go to https://www.tesla.com/
       driver.get("https://www.tesla.com/")

       # 2. Click on the button "Energy" on the header menu
       energy_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
       energy_button.click()
       time.sleep(3)

       # 3. Check if the new window contains title "Energy"
       self.assertIn("Energy", driver.title)
       time.sleep(4)

       # 4.  Click on the "Solar Panels" element
       solar_panels_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
       solar_panels_button.click()
       time.sleep(4)

       # 5. Check if the new window contains title "Solar Panels"
       self.assertIn("Solar Panels", driver.title)

       #  Scroll down to find the "Support" button on the header menu
       driver.execute_script("window.scrollTo(0, 1500)")
       time.sleep(3)

       # 6. Click on the "Support" button
       support_button = WebDriverWait(driver, 5).until(
           EC.element_to_be_clickable((By.XPATH, "//span[@class='tds-text--700'][contains(.,'Support')]")))
       support_button.click()
       time.sleep(2)

       # 7. Check if the new window contains title "Support"
       self.assertIn("Support", driver.title)

       # 8. Type "ncjifehhrehfl" in the "Support Search" section
       support_search_input = WebDriverWait(driver, 5).until(
           EC.presence_of_element_located((By.XPATH, "//input[@id='support-search-input']")))
       support_search_input.send_keys("ncjifehhrehfl")
       time.sleep(5)

       # 9. Click "Enter" button
       support_search_input.send_keys(Keys.ENTER)
       time.sleep(3)

       # 10. Verify that the elements provided in search page are not present
       results = driver.find_element(By.XPATH, '//*[@id="results-container"]/div/h2')
       if results:
           print("No search results with keyword fjhghhjhg- Test Case 025 passed")
       else:
            print("Results with keyword fjhghhjhg are available- Test Case 025 failed")


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

        # Test case 021 positive. Verify that "Energy" button is clickable and transfer to correct page.

    def test_case_021_positive_energy_page(self):
        driver = self.driver

        print("Test Case 021")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")
        driver.maximize_window()

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        print("Energy is available- Test case 021 passed")


        # Test case 022 positive.  Validate that "Solar Roof" element is visible in the header and  is clickable

    def test_case022_positive_solar_roof_button(self):
        driver = self.driver

        print("Test Case 022")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(4)

        # 3. Click "Solar Roof" element on the menu page
        solar_roof_button = driver.find_element(By.XPATH, "//img[@alt ='Solar Roof']")
        solar_roof_button.click()
        delay()

        # 4.Check if the new window contains title "Solar Roof"
        self.assertIn("Solar Roof", driver.title)
        print("SolarRoof is available- Test case 022 passed")


        # Test Case 023 positive.  Navigate to Megapack and test "Order Now" button

    def test_case023_positive_megapack_order_page(self):
        driver = self.driver

        print("Test Case 023")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the "Energy" button on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(5)

        # 3. Click "Megapack" element on the menu page
        megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
        megapack_button.click()
        delay()

        # 4. Check if the new window contains title "Megapack"
        self.assertIn("Megapack", driver.title)

        # 5. Click on the "Order Now" button
        order_now_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tesla-hero-5114"]/div[2]/div/section/div')))
        order_now_button.click()
        delay()

        # 6. Verify that the "Order Now" is functional and page has loaded successfully
        self.assertIn("Order Megapack", driver.title)
        print("Order Megapack is available-Test case 023 passed")


        # Test Case 024 positive.  Navigate to Megapack page and test "Video" on the page

    def test_case024_positive_megapack_video_page(self):
        driver = self.driver

        print("Test Case 024")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the "Energy" button on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Click "Megapack" element on the menu page
        megapack_button = driver.find_element(By.XPATH, '//img[@alt ="Megapack"]')
        megapack_button.click()
        delay()

        # 4. Check if the new window contains title "Megapack"
        self.assertIn("Megapack", driver.title)

        # 5. Find the first video on the page "Megapack"
        driver.execute_script("window.scrollTo(0,2800)")
        time.sleep(5)
        video = driver.find_element(By.XPATH,
                                    '//*[@id="tesla-text-with-media-137"]/section/section[1]/div/div/video')
        driver.save_screenshot("video1.png")
        video.click()
        time.sleep(6)
        driver.save_screenshot("video2.png")
        print("video is playing.Check Screenshots.- Test Case 024 passed")


        # Test Case 025 positive.  Navigate to "Powerwall" page and Validate that page have access to translator page
        # in "Romana"

    def test_case025_positive_powerwall_page_română(self):
        driver = self.driver

        print("Test Case 025")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Click on the " Powerwall" element
        powerwall_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Powerwall']")))
        powerwall_button.click()
        time.sleep(2)

        # 4. Check if the new window contains title "Powerwall"
        self.assertIn("Powerwall", driver.title)
        time.sleep(3)

        # 5.Click on "globe" button
        globe_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='dx-nav-item--locale-selector']")))
        globe_button.click()
        time.sleep(2)

        # 6. Select "Română" language
        română_language_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Română')]")))
        română_language_button.click()
        time.sleep(3)

        # 7. Verify if the page is in "Română"by checking the page title or specific content
        error_message = driver.find_element(By.XPATH, "//h1[@class='error-code'][contains(.,'404')]")
        if 404 and error_message:
            print("Test case 025 fail")
        else:
            print("Test case 025 passed")


        # Test Case 021 negative. Validate that in the "Solar Panels" page is possible to access  "Order Now " button and
        # can't click "Next" without provide any user information

    def test_case021_negative_solar_panels_order_now_page(self):
        driver = self.driver

        print("Test Case 021 Negative")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        time.sleep(4)

        # 4. Click on the "Solar Panels" element
        solar_panels_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
        solar_panels_button.click()
        time.sleep(4)

        # 5. Click on the "Order Now" button
        order_now_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[1]")))
        order_now_button.click()
        time.sleep(3)

        # 4. Check if the new window contains title "Design your Solar"
        self.assertIn("Design your Solar", driver.title)
        time.sleep(3)

        # 6. Scroll down to find and click "Next" button without including any information
        driver.execute_script("window.scrollTo(0,1600)")
        time.sleep(5)

        # 7. Try to click "Next" without entering any user information
        next_button = driver.find_element(By.XPATH, '//*[@id="landing-page-next-btn"]')
        next_button.click()
        time.sleep(3)

        # 8. Verify that the "Next" button doesn't allow navigation without user input
        is_disabled = next_button.get_attribute('disabled') is not None
        print(is_disabled)
        if is_disabled:
            print("Button is displayed.Test Case 021 passed")
        else:
            print("Button is not displayed. Test Case 021 negative failed")  # Passed

        # Test Case 022 negative.  Validate that in the "Solar Panels" page is possible to access  "Chat " button and
        # can't request a Call Back without provide any user information

    def test_case022_negative_solar_panels_chat_request_callback(self):
        driver = self.driver

        print("Test Case 022 Negative")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        time.sleep(4)

        # 4.  Click on the "Solar Panels" element
        solar_panels_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
        solar_panels_button.click()
        time.sleep(4)

        # 5. Check if the new window contains title "Solar Panels"
        self.assertIn("Solar Panels", driver.title)

        # 6. Click on the "Chat" button
        chat_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
        chat_button.click()
        time.sleep(3)

        # 7. Scroll down to find the "Request a Callback" button
        chat_box = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]')
        actions = ActionChains(driver)
        actions.move_to_element(chat_box).click().send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(5)

        # 8. Click "Request A Callback" button without including any user information
        callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
        is_disabled = callback_button.get_attribute('disabled') is not None
        print(is_disabled)
        if is_disabled:
            print("Button is disable. Test case 022 passed")
        else:
            print("Button is not disable. Test case 022 failed")  # Pass

        # Test Case 023 negative. Validate that in the "Solar Panels " page the user enter wrong elements in  Last and
        #  First Name box and can't  do the order

    def test_case023_negative_solar_panels_chat_request_callback_invalid_name(self):
        driver = self.driver

        print("Test Case 023 Negative")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        time.sleep(4)

        # 4.  Click on the "Solar Panels" element
        solar_panels_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
        solar_panels_button.click()
        time.sleep(4)

        # 5. Check if the new window contains title "Solar Panels"
        self.assertIn("Solar Panels", driver.title)

        # 6. Click on the "Chat" button
        chat_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
        chat_button.click()
        time.sleep(3)

        # 7. Verify that the chat window is opened by checking for some chat-specific element
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
        time.sleep(2)

        # 8. Fill in the required information field with invalid name
        first_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
        first_name_input.send_keys("345565@#$%hijkj")
        time.sleep(2)

        last_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
        last_name_input.send_keys("tyuuhi^&^$#!@123")
        time.sleep(2)

        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        email_input.send_keys("jepapad460@esterace.com")
        time.sleep(2)

        phone_number_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
        phone_number_input.send_keys("15674852769")
        time.sleep(2)

        zip_code_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
        zip_code_input.send_keys("78965")
        time.sleep(3)

        product_interest_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
        product_interest_input.send_keys("Solar Panels")
        time.sleep(2)

        # 9. Click "Request A Callback" button
        request_callback_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Request a Callback')]")))
        request_callback_button.click()
        time.sleep(3)

        # 10. Verify that the page is not allowed to go next
        confirmation_message = driver.find_element(By.XPATH, '//*[@id="avaya-chat-modal"]/div/div[1]').text
        print(confirmation_message)
        if "Thank you!" in confirmation_message:
            print(" Thank you! We will contact your soon- Test case 023 failed")
        else:
            print("Confirmation message is not present.  Test Case 023 passed")


        # Test case 024 negative. Validate that in the "Solar Panels" page the user can't send to "Request A Callback"
        # without email address

    def test_case024_negative_solar_panels_chat_request_callback_no_email(self, ):
        driver = self.driver

        print("Test Case 024 Negative")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        time.sleep(4)

        # 4.  Click on the "Solar Panels" element
        solar_panels_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
        solar_panels_button.click()
        time.sleep(4)

        # 5. Check if the new window contains title "Solar Panels"
        self.assertIn("Solar Panels", driver.title)

        # 6. Click on the "Chat" button
        chat_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")))
        chat_button.click()
        time.sleep(3)

        # 7. Verify that the chat window is opened by checking for some chat-specific element
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//header[contains(.,'Chat')]")))
        time.sleep(2)

        # 8. Fill in the required information field with invalid name
        first_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
        first_name_input.send_keys(" Ella")
        time.sleep(2)

        last_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']")))
        last_name_input.send_keys(" Smith")
        time.sleep(2)

        phone_number_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']")))
        phone_number_input.send_keys("15674852769")
        time.sleep(2)

        zip_code_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='zip']")))
        zip_code_input.send_keys("78965")
        time.sleep(3)

        product_interest_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='SolarPanels']")))
        product_interest_input.send_keys("Solar Panels")
        time.sleep(3)

        # 9. Click "Request A Callback" button without including user email address information
        callback_button = driver.find_element(By.XPATH, '//*[@id="chat-page"]/form/button')
        is_disabled = callback_button.get_attribute('disabled') is not None
        print(is_disabled)
        if is_disabled:
            print("Button is disable without email address information. Test case 022 passed")
        else:
            print("Button is not disable. Test case 022 failed")  # Pass

        # Test Case  025 Negative. Validate if the "Support" button is clickable on the "Solar Panels page is not
        # accessible if introducing wrong data in "Support Search" line

    def test_case025_negative_solar_panels_support_search(self):
        driver = self.driver

        print("Test Case 025 Negative")

        # 1. Go to https://www.tesla.com/
        driver.get("https://www.tesla.com/")

        # 2. Click on the button "Energy" on the header menu
        energy_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//header/ol[1]/li[2]/button[1]/span[1]")))
        energy_button.click()
        time.sleep(3)

        # 3. Check if the new window contains title "Energy"
        self.assertIn("Energy", driver.title)
        time.sleep(4)

        # 4.  Click on the "Solar Panels" element
        solar_panels_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'Solar Panels')]")))
        solar_panels_button.click()
        time.sleep(4)

        # 5. Check if the new window contains title "Solar Panels"
        self.assertIn("Solar Panels", driver.title)

        #  Scroll down to find the "Support" button on the header menu
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(3)

        # 6. Click on the "Support" button
        support_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='tds-text--700'][contains(.,'Support')]")))
        support_button.click()
        time.sleep(2)

        # 7. Check if the new window contains title "Support"
        self.assertIn("Support", driver.title)

        # 8. Type "ncjifehhrehfl" in the "Support Search" section
        support_search_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='support-search-input']")))
        support_search_input.send_keys("ncjifehhrehfl")
        time.sleep(5)

        # 9. Click "Enter" button
        support_search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # 10. Verify that the elements provided in search page are not present
        results = driver.find_element(By.XPATH, '//*[@id="results-container"]/div/h2')
        if results:
            print("No search results with keyword fjhghhjhg- Test Case 025 passed")
        else:
            print("Results with keyword fjhghhjhg are available- Test Case 025 failed ")


def tearDown(self):
   self.driver.quit()


if __name__ == "__main__":
   unittest.main()
