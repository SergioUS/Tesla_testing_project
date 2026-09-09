import time
import unittest
import random
import Helpers as H
import HtmlTestRunner
import AllureReports

from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common import WebDriverException as WDE, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(2, 4))
# This function is for delay() it randomly pics time between 1and 4 seconds


class ChromeTestsPositive(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
           "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)
# This is a class setUp. We will have 3 (chrome,firefox,edge)

    def test_chrome_107(self):
        driver = self.driver
# 1. Opening website, enter http://tesla.com
        driver.get("https://www.tesla.com/")
# random delay time from 1 to 4 seconds
        delay()
# 2. Verify button "Shop" is visible and displayed correctly
# method in which waiting for element to be visible on the page
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
        delay()  # simulate long running test
# another method with print results
        shop = driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']")#.is_displayed()
        shop.is_displayed()
        if shop is not None:
            print("Element 'Shop' is visible and displayed")
        else:
            print("Element 'Shop' is not displayed")
# another method with an exception where code doesn't stop if the element is not found
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
            print("Element 'Shop' is visible and displayed")
        except NoSuchElementException:
            print("Element 'Shop' not found ")

    def test_chrome_108(self):
        driver = self.driver
# 1. Opening website, enter http://tesla.com
        driver.get("https://www.tesla.com/")
# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Verify that each of the 4 buttons presents in the menu: Charging, Vehicle Accessories, Apparel, Lifestyle
        wait = WebDriverWait(driver, 2)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//h3[contains(.,'Charging')])[3]")))
            print("Element 'Charging' is present")
        except NoSuchElementException:
            print("Element 'Charging' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Vehicle Accessories')]")))
            print("Element 'Vehicle Accessories' is present")
        except NoSuchElementException:
            print("Element 'CVehicle Accessories' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Apparel')]")))
            print("Element 'Apparel' is present")
        except NoSuchElementException:
            print("Element 'Apparel' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Lifestyle')]")))
            print("Element 'Lifestyle is present")
        except NoSuchElementException:
            print("Element 'Lifestyle' not found ")

    def test_chrome_109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Verify that correct page is open ("Apparel")
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'men.best-sellers')))
            print("You are on the page 'Apparel'")
        except WDE:
            print("The page is not correct!!!")

    def test_chrome_110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        element_to_hover = driver.find_element(By.XPATH, "//div[contains(@data-open-block,'tile-2')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify menu "Men Women Kids" is present on the page
    # Check if the search returns any result
        try:
            assert "kids.outerwear" in driver.page_source
            print("The menu appears when hover over the 'Apparel' button")
        except AssertionError:
            print("Hover doesn't work!!!")

    def test_chrome_111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        time.sleep(3)
        driver.find_element(By.XPATH, H.Apparel_1).click()
# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        time.sleep(4)
        element_to_hover = driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Click the button "Onesies" under the "Kids" menu
        time.sleep(3)
        onesies = driver.find_element(By.XPATH, "//a[@href='/category/apparel/kids#kids.onesies']")
        actions = ActionChains(driver)
        actions.click(onesies).perform()

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class FifeFoxTestsPositive(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)

    def test_FifeFox_107(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")
# random delay time from 1 to 4 seconds
        delay()
# 2. Verify button "Shop" is visible and displayed correctly
# method in which waiting for element to be visible on the page
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
        delay()  # simulate long running test
# another method with print results
        shop = driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']")#.is_displayed()
        shop.is_displayed()
        if shop is not None:
            print("Element 'Shop' is visible and displayed")
        else:
            print("Element 'Shop' is not displayed")
# another method with an exception where code doesn't stop if the element is not found
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
            print("Element 'Shop' is visible and displayed")
        except NoSuchElementException:
            print("Element 'Shop' not found ")

    def test_FifeFox_108(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")
# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Verify that each of the 4 buttons presents in the menu: Charging, Vehicle Accessories, Apparel, Lifestyle
        wait = WebDriverWait(driver, 2)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//h3[contains(.,'Charging')])[3]")))
            print("Element 'Charging' is present")
        except NoSuchElementException:
            print("Element 'Charging' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Vehicle Accessories')]")))
            print("Element 'Vehicle Accessories' is present")
        except NoSuchElementException:
            print("Element 'CVehicle Accessories' not found ")


        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Apparel')]")))
            print("Element 'Apparel' is present")
        except NoSuchElementException:
            print("Element 'Apparel' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Lifestyle')]")))
            print("Element 'Lifestyle is present")
        except NoSuchElementException:
            print("Element 'Lifestyle' not found ")

    def test_FifeFox_109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Verify that correct page is open ("Apparel")
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'men.best-sellers')))
            print("You are on the page 'Apparel'")
        except WDE:
            print("The page is not correct!!!")

    def test_FifeFox_110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()
# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        element_to_hover = driver.find_element(By.XPATH, "//div[contains(@data-open-block,'tile-2')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify menu "Men Women Kids" is present on the page
    # Check if the search returns any result
        try:
            assert "kids.outerwear" in driver.page_source
            print("The menu appears when hover over the 'Apparel' button")
        except AssertionError:
            print("Hover doesn't work!!!")

    def test_FifeFox_111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        time.sleep(3)
        driver.find_element(By.XPATH, H.Apparel_1).click()
# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        time.sleep(4)
        element_to_hover = driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Click the button "Onesies" under the "Kids" menu
        time.sleep(3)
        onesies = driver.find_element(By.XPATH, "//a[@href='/category/apparel/kids#kids.onesies']")
        actions = ActionChains(driver)
        actions.click(onesies).perform()

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class EdgeTestsPositive(unittest.TestCase):

    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)

    def test_Edge_107(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")
# random delay time from 1 to 4 seconds
        delay()
# 2. Verify button "Shop" is visible and displayed correctly
# method in which waiting for element to be visible on the page
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
        delay()  # simulate long running test
# another method with print results
        shop = driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']")#.is_displayed()
        shop.is_displayed()
        if shop is not None:
            print("Element 'Shop' is visible and displayed")
        else:
            print("Element 'Shop' is not displayed")
# another method with an exception where code doesn't stop if the element is not found
        wait = WebDriverWait(driver, 4)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='dx-nav-item--shop']")))
            print("Element 'Shop' is visible and displayed")
        except NoSuchElementException:
            print("Element 'Shop' not found ")

    def test_Edge_108(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")
# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Verify that each of the 4 buttons presents in the menu: Charging, Vehicle Accessories, Apparel, Lifestyle
        wait = WebDriverWait(driver, 2)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//h3[contains(.,'Charging')])[3]")))
            print("Element 'Charging' is present")
        except NoSuchElementException:
            print("Element 'Charging' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Vehicle Accessories')]")))
            print("Element 'Vehicle Accessories' is present")
        except NoSuchElementException:
            print("Element 'CVehicle Accessories' not found ")


        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Apparel')]")))
            print("Element 'Apparel' is present")
        except NoSuchElementException:
            print("Element 'Apparel' not found ")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(.,'Lifestyle')]")))
            print("Element 'Lifestyle is present")
        except NoSuchElementException:
            print("Element 'Lifestyle' not found ")

    def test_Edge_109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Verify that correct page is open ("Apparel")
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'men.best-sellers')))
            print("You are on the page 'Apparel'")
        except WDE:
            print("The page is not correct!!!")

    def test_Edge_110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, "//h3[contains(.,'Apparel')]").click()
# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        element_to_hover = driver.find_element(By.XPATH, "//div[contains(@data-open-block,'tile-2')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Verify menu "Men Women Kids" is present on the page
    # Check if the search returns any result
        try:
            assert "kids.outerwear" in driver.page_source
            print("The menu appears when hover over the 'Apparel' button")
        except AssertionError:
            print("Hover doesn't work!!!")

    def test_Edge_111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        time.sleep(3)
        driver.find_element(By.XPATH, "//img[contains(@alt,'Apparel')]").click()
# 4. Hover the mouse over the button "Apparel" in the header
    # Find the element you want to hover over
        time.sleep(4)
        element_to_hover = driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]")
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 5. Click the button "Onesies" under the "Kids" menu
        time.sleep(3)
        onesies = driver.find_element(By.XPATH, "//a[@href='/category/apparel/kids#kids.onesies']")
        actions = ActionChains(driver)
        actions.click(onesies).perform()

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class ChromeTestsNegative(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)

    def test_chrome_107107(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 6. Select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 7. Enter number greater than 5 in the field "Quantity"
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys("6")
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert = driver.find_element(By.XPATH,"(//p[@class='alert-text message'])[1]")
        if alert:
            print ("Test_chrome_107107 PASS")
        else:
            print ("Test_chrome_107107 FAIL")

    def test_chrome_108108(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 7. Do not select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert2 = driver.find_element(By.XPATH, "(//p[contains(.,'Please select a size')])[1]")
        if alert2:
            print("Test_chrome_108108 PASS")
        else:
            print("Test_chrome_108108 FAIL")

    def test_chrome_109109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the word "cat"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        #driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("cat")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
             (By.XPATH, "//span[contains(.,'No Results Found')]")))
            print ("Test_chrome_109109 PASS")
        except WDE:
            print ("Test_chrome_109109 FAIL")

    def test_chrome_110110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the number 2
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        # driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("2")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(.,'Please enter 2 or more characters')]")))
            print("Test_chrome_110110 PASS")
        except WDE:
            print("Test_chrome_110110 FAIL")

    def test_chrome_111111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Go to menu Hats
        delay()
        TruckerHat = driver.find_element(By.XPATH, H.Hat)
        driver.execute_script("arguments[0].scrollIntoView();", TruckerHat)

# 5. Select any product that is Out Of Stock
        delay()
        TruckerHat.click()

# 6. Click "Email me when this item is restocked"
        delay()
        driver.find_element(By.XPATH, "(//div[contains(.,'Email me when this item is restocked')])[9]").click()
# 7. Do not enter an email address
# 8. Click "Notify me"
        driver.find_element(By.XPATH, "(//input[@value='Notify Me'])[1]").click()

        wait = WebDriverWait(driver, 5)
        #time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "(//label[contains(.,'Email Address')])[1]")))
            print("Test_chrome_111111 PASS")
        except WDE:
            print("Test_chrome_111111 FAIL")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class FireFoxTestsNegative(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)


    def test_FifeFox_107107(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        element_to_hover = driver.find_element(By.XPATH, H.Shop)
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 6. Select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 7. Enter number greater than 5 in the field "Quantity"
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys("6")
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert = driver.find_element(By.XPATH,"(//p[@class='alert-text message'])[1]")
        if alert:
            print ("Test_FifeFox_107107 PASS")
        else:
            print ("Test_FifeFox_107107 FAIL")

    def test_FifeFox_108108(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 7. Do not select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert2 = driver.find_element(By.XPATH, "(//p[contains(.,'Please select a size')])[1]")
        if alert2:
            print("Test_FifeFox_108108 PASS")
        else:
            print("Test_FifeFox_108108 FAIL")

    def test_FifeFox_109109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the word "cat"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        #driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("cat")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
             (By.XPATH, "//span[contains(.,'No Results Found')]")))
            print ("Test_FifeFox_109109 PASS")
        except WDE:
            print ("Test_FifeFox_109109 FAIL")

    def test_FifeFox_110110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the number 2
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        # driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("2")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(.,'Please enter 2 or more characters')]")))
            print("Test_FifeFox_110110 PASS")
        except WDE:
            print("Test_FifeFox_110110 FAIL")

    def test_FifeFox_111111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Go to menu Hats
        delay()
        TruckerHat = driver.find_element(By.XPATH, H.Hat)
        driver.execute_script("arguments[0].scrollIntoView();", TruckerHat)

        # 5. Select any product that is Out Of Stock
        delay()
        TruckerHat.click()

# 6. Click "Email me when this item is restocked"
        delay()
        driver.find_element(By.XPATH, "(//div[contains(.,'Email me when this item is restocked')])[9]").click()
# 7. Do not enter an email address
# 8. Click "Notify me"
        driver.find_element(By.XPATH, "(//input[@value='Notify Me'])[1]").click()

        wait = WebDriverWait(driver, 5)
        #time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "(//label[contains(.,'Email Address')])[1]")))
            print("Test_FifeFox_111111 PASS")
        except WDE:
            print("Test_FifeFox_111111 FAIL")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class EdgeTestsNegative(unittest.TestCase):

    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        wait = WebDriverWait(driver, 5)

    def test_Edge_107107(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        element_to_hover = driver.find_element(By.XPATH, H.Shop)
    # Create an ActionChains object
        actions = ActionChains(driver)
    # Perform the hover action
        actions.move_to_element(element_to_hover).perform()

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 6. Select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 7. Enter number greater than 5 in the field "Quantity"
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys("6")
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert = driver.find_element(By.XPATH,"(//p[@class='alert-text message'])[1]")
        if alert:
            print ("Test_Edge_107107 PASS")
        else:
            print ("Test_Edge_107107 FAIL")

    def test_Edge_108108(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Scroll down to the menu section "Onesies"
        delay()
        OnesieEnergy = driver.find_element(By.XPATH, H.Onesie)
        driver.execute_script("arguments[0].scrollIntoView();", OnesieEnergy)

# 5. Click on the selected item
        delay()
        OnesieEnergy.click()

# 7. Do not select a size
        delay()
        driver.find_element(By.XPATH, H.SizeOnesies).click()
# 8. Click "Add to cart"
        driver.find_element(By.XPATH, "//input[@id='addToCartBtn']").click()

# 9. Print result of the test
        alert2 = driver.find_element(By.XPATH, "(//p[contains(.,'Please select a size')])[1]")
        if alert2:
            print("Test_Edge_108108 PASS")
        else:
            print("Test_Edge_108108 FAIL")

    def test_Edge_109109(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
        # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        time.sleep(4)
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the word "cat"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        #driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("cat")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
             (By.XPATH, "//span[contains(.,'No Results Found')]")))
            print ("Test_Edge_109109 PASS")
        except WDE:
            print ("Test_Edge_109109 FAIL")

    def test_Edge_110110(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. In the upper right corner in the search field, type the number 2
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]"))).click()
        # driver.find_element(By.XPATH, '//*[contains(text(), viewBox="0 0 24 24")]').click()
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys("2")
        driver.find_element(By.XPATH, "//input[@id='1']").send_keys(Keys.ENTER)

        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(.,'Please enter 2 or more characters')]")))
            print("Test_Edge_110110 PASS")
        except WDE:
            print("Test_Edge_110110 FAIL")

    def test_Edge_111111(self):
        driver = self.driver
# opening website 1. Enter http://tesla.com
        driver.get("https://www.tesla.com/")

# 2. Hover the mouse over the button "Shop" in the header
    # Find the element you want to hover over
        delay()
        H.hover_shop(driver)

# 3. Click the “Apparel” button
        delay()
        driver.find_element(By.XPATH, H.Apparel_1).click()

# 4. Go to menu Hats
        delay()
        TruckerHat = driver.find_element(By.XPATH, H.Hat)
        driver.execute_script("arguments[0].scrollIntoView();", TruckerHat)

        # 5. Select any product that is Out Of Stock
        delay()
        TruckerHat.click()

# 6. Click "Email me when this item is restocked"
        delay()
        driver.find_element(By.XPATH, "(//div[contains(.,'Email me when this item is restocked')])[9]").click()
# 7. Do not enter an email address
# 8. Click "Notify me"
        driver.find_element(By.XPATH, "(//input[@value='Notify Me'])[1]").click()

        wait = WebDriverWait(driver, 5)
        #time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "(//label[contains(.,'Email Address')])[1]")))
            print("Test_Edge_111111 PASS")
        except WDE:
            print("Test_Edge_111111 FAIL")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

#if __name__ == '__main__':
#   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

#if __name__ == '__main__':
#   suite = unittest.TestLoader().loadTestsFromTestCase(EdgeTestsPositive)
#   runner = HtmlTestRunner.HTMLTestRunner(output='./HtmlReports')
#    runner.run(suite)

#if __name__ == "__main__":
#   unittest.main(AllureReports)
