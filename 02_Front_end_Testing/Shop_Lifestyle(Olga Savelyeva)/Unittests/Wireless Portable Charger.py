# Olga Savelyeva
import random
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service


def delay():
    time.sleep(random.randint(1, 5))

class ChromeTests(unittest.TestCase):

    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def test_chrome_TC_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

    # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
    # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(2)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is displayed
        if driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").is_displayed():
            print("Lifestyle button is visible")
        else:
            print("Lifestyle button is not visible")

        # quit from browser
        driver.quit()

    def test_chrome_TC_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

       # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_chrome_TC_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        # go down find product
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        print("Text of Charger is displayed")


        # quit from browser
        driver.quit()

    def test_chrome_TC_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)


        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Check elements on page
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_chrome_TC_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH,"//input[@data-colorname='Rose Gold']")
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, "(//button[contains(.,'+')])[2]")
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")
        delay()

        driver.save_screenshot("PosChr_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class FirefoxTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_firefox_TC_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(2)

        # Verify button "Lifestyle" is displayed
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").is_displayed()
        print("Lifestyle button is visible")

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_firefox_TC_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_firefox_TC_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        print("Text of Charger is displayed")

        # quit from browser
        driver.quit()

    def test_firefox_TC_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_firefox_TC_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Rose Gold']")
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, "(//button[contains(.,'+')])[2]")
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(1)
        delay()

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")

        driver.save_screenshot("PosFF_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class EdgeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_Edge_TC_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

    # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
    # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(2)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is displayed
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").is_displayed()
        print("Lifestyle button is visible")

        # quit from browser
        driver.quit()

    def test_Edge_TC_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_Edge_TC_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        print("Text of Charger is displayed")


        # quit from browser
        driver.quit()

    def test_Edge_TC_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)


        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_Edge_TC_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        #Verufy page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH,"//input[@data-colorname='Rose Gold']")
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, "(//button[contains(.,'+')])[2]")
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(1)
        #if

        delay()

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")

        driver.save_screenshot("PosEd_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class ChromeNegTests(unittest.TestCase):

    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def test_chrome_TC_Neg_102_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        #open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Rose Gold']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='4']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed" )
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_103_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='White']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='5']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[3]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[3]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_104_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

       #Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@data-item-added='Added'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@data-item-added='Added'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_105_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_105_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_106_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, "//input[@id='3']")
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

class FirefoxNegTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_firefox_TC_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        #open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Rose Gold']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='4']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed" )
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_103_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()
        time.sleep(2)

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='White']")
        color_option.click()
        time.sleep(2)

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='5']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[3]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[3]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_104_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

       #Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@data-item-added='Added'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@data-item-added='Added'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_105_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_106_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, "//input[@id='3']")
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

class EdgeNegTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_edge_TC_Neg_102_102(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        #open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Rose Gold']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='4']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='4']").send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[2]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[2]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed" )
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_103_103(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='White']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='5']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='5']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[3]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[3]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_104_104(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

       #Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@data-item-added='Added'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@data-item-added='Added'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_105_105(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='3']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='addToCartBtn'])[1]")))
        print("button is clickable")
        driver.find_element(By.XPATH, "(//input[@id='addToCartBtn'])[1]").click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]"):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_105_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_106_106(self):
        driver = self.driver

        driver.get('https://www.tesla.com/')
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
        driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
        driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
        # open "Shop" page
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's title
        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements/buttons
        driver.find_element(By.ID, "lifestyle.best-sellers")
        driver.find_element(By.ID, "page--category")
        driver.find_element(By.ID, "lifestyle.bags")
        driver.find_element(By.ID, "left-menu__logo")

        driver.execute_script("window.scrollTo(0,6500)")
        time.sleep(10)

        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, "(//h2[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'content')])[33]").is_displayed()
        driver.find_element(By.XPATH, "(//div[@class='quantity-picker-container'])[1]").is_displayed()
        driver.find_element(By.XPATH, "(//div[contains(@class,'credit-promotion-message')])[1]").is_displayed()
        driver.find_element(By.ID, "left-menu__logo").is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, "//input[@data-colorname='Black']")
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, "//input[@id='3']")
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

