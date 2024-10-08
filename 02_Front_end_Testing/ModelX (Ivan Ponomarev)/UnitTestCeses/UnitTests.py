import time
import unittest
import random
from webbrowser import Edge
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
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
from selenium.webdriver import requests
from webdriver_manager.drivers.edge import EdgeChromiumDriver

def delay():
    time.sleep(random.randint(1, 5))
class ChromePositiveNegativeTests(unittest.TestCase):
    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_TC_016(self):
        driver = self.driver
        print("positive TC-016")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        if driver.title == "Model X | Tesla":
            print("TC-016 pass. Model X page is open correctly")
        else:
            print("TC-016 fail")
        driver.quit()

    def test_TC_017(self, current_url=None):
        driver = self.driver
        print("positive TC-017")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//label[contains(@for,'PR01')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Six Seat Interior')]").click()
        delay()
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Order Now')]")
            if element:
                print("TC-017 pass. The users can customize their vehicle.")
            else:
                print("TC-017 fail. The users can't customize their vehicle.")
        except NoSuchElementException:
            print("TC-017 fail.")

    def test_TC_018(self):
        driver = self.driver
        print("positive TC-018")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']").click()
        time.sleep(6)
        try:
            shop_now = driver.find_element(By.XPATH, "//a[contains(@aria-describedby,'hero-0')]")
            if shop_now:
                print('TC-18 pass. "Shop now" button clickable.')
            else:
                print('TC-18 fail. "Shop now" button unclickable.')
        except NoSuchElementException:
                print("TC-18 fail.")

    def test_TC_019(self):
        driver = self.driver
        print("positive TC-019")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        try:
            element = driver.find_element(By.XPATH, "(//a[contains(@title,'Help Me Choose')])[1]")
            if element:
                print('TC-019 pass. "Compare Models" page loads correctly with all elements visible.')
            else:
                print('TC-019 fail. "Compare Models" page does not loads correctly.')
        except NoSuchElementException:
            print("TC-019 fail.")

    def test_TC_020(self):
        driver = self.driver
        print("positive TC-020")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Add Model')]")
            if element:
                print('TC-020 pass. Customer can compare Tesla Models')
            else:
                print('TC-020 fail. Customer can not compare Tesla Models')
        except NoSuchElementException:
            print("TC-020 fail.")

    def test_TC_016_16(self):
        driver = self.driver
        print("negative TC_016_16")
        driver.get("https://www.tesla.com/modelx/qwerty")
        error_code = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[1]')
        error_text = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[2]')
        if error_code and error_text:
            print('"404" and page not found message is visible. Test pass.')
        else:
            print("No error message. test fail")

    def test_TC_017_17(self, current_url=None):
        driver = self.driver
        print("negative TC_017_17")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        firstname_field = driver.find_element(By.XPATH, '//*[@id="FIRST_NAME"]')
        orig_name = firstname_field.get_attribute("maxlength")
        print(orig_name)
        first_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_first_name = len(first_name)
        print(length_of_first_name)
        firstname_field.send_keys(first_name)
        time.sleep(3)
        length_result = firstname_field.get_attribute("value")
        final_result = len(length_result)
        print(length_of_first_name, final_result)
        if final_result == 50:
            print("test_TC_017_17 pass")
        else:
            print("test_TC_017_17 fail")

    def test_TC_018_18(self, current_url=None):
        driver = self.driver
        print("negative TC_018_18")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        lastname_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
        orig_name = lastname_field.get_attribute("maxlength")
        print(orig_name)
        last_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_last_name = len(last_name)
        print(length_of_last_name)
        lastname_field.send_keys(last_name)
        time.sleep(3)
        length_result = lastname_field.get_attribute("value")
        final_result1 = len(length_result)
        print(length_of_last_name, final_result1)
        if final_result1 == 50:
            print("test_TC_018_18 pass")
        else:
            print("test_TC_018_18 fail")

    def test_TC_019_19(self):
        driver = self.driver
        print("negative TC_019_19")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        firstname_input = driver.find_element(By.XPATH, "//input[contains(@name,'firstName')]")
        invalid_name = "398392Q!@3"
        firstname_input.clear()
        firstname_input.send_keys(invalid_name)
        firstname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_019_19 fail. No error message when input incorrect symbols in "First name" field.')
        else:
            print('test_TC_019_19 pass. Error message "Invalid name" is right under "First name" field.')

    def test_TC_020_20(self):
        driver = self.driver
        print("negative TC_020_20")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        invalid_name = "qWA!#@#@!!8183881"
        lastname_input.clear()
        lastname_input.send_keys(invalid_name)
        lastname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_020_20 fail. No error message when input incorrect symbols in "Last name" field.')
        else:
            print('test_TC_020_20 pass. Error message "Invalid name" is right under "Last name" field.')

def delay():
    time.sleep(random.randint(1, 5))

class EdgePositiveNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()

    def test_TC_016(self):
        driver = self.driver
        print("positive TC-016")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        if driver.title == "Model X | Tesla":
            print("TC-016 pass. Model X page is open correctly")
        else:
            print("TC-016 fail")

    def test_TC_017(self, current_url=None):
        driver = self.driver
        print("positive TC-017")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//label[contains(@for,'PR01')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Six Seat Interior')]").click()
        delay()
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Order Now')]")
            if element:
                print("TC-017 pass. The users can customize their vehicle.")
            else:
                print("TC-017 fail. The users can't customize their vehicle.")
        except NoSuchElementException:
            print("TC-017 fail.")

    def test_TC_018(self):
        driver = self.driver
        print("positive TC-018")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']").click()
        time.sleep(6)
        try:
            shop_now = driver.find_element(By.XPATH, "//a[contains(@aria-describedby,'hero-0')]")
            if shop_now:
                print('TC-18 pass. "Shop now" button clickable.')
            else:
                print('TC-18 fail. "Shop now" button unclickable.')
        except NoSuchElementException:
                print("TC-18 fail.")

    def test_TC_019(self):
        driver = self.driver
        print("positive TC-019")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        try:
            element = driver.find_element(By.XPATH, "(//a[contains(@title,'Help Me Choose')])[1]")
            if element:
                print('TC-019 pass. "Compare Models" page loads correctly with all elements visible.')
            else:
                print('TC-019 fail. "Compare Models" page does not loads correctly.')
        except NoSuchElementException:
            print("TC-019 fail.")

    def test_TC_020(self):
        driver = self.driver
        print("positive TC-020")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Add Model')]")
            if element:
                print('TC-020 pass. Customer can compare Tesla Models')
            else:
                print('TC-020 fail. Customer can not compare Tesla Models')
        except NoSuchElementException:
            print("TC-020 fail.")

    def test_TC_016_16(self):
        driver = self.driver
        print("negative TC_016_16")
        driver.get("https://www.tesla.com/modelx/qwerty")
        error_code = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[1]')
        error_text = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[2]')
        if error_code and error_text:
            print('"404" and page not found message is visible. Test pass.')
        else:
            print("No error message. test fail")

    def test_TC_017_17(self, current_url=None):
        driver = self.driver
        print("negative TC_017_17")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        firstname_field = driver.find_element(By.XPATH, '//*[@id="FIRST_NAME"]')
        orig_name = firstname_field.get_attribute("maxlength")
        print(orig_name)
        first_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_first_name = len(first_name)
        print(length_of_first_name)
        firstname_field.send_keys(first_name)
        time.sleep(3)
        length_result = firstname_field.get_attribute("value")
        final_result = len(length_result)
        print(length_of_first_name, final_result)
        if final_result == 50:
            print("test_TC_017_17 pass")
        else:
            print("test_TC_017_17 fail")

    def test_TC_018_18(self, current_url=None):
        driver = self.driver
        print("negative TC_018_18")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        lastname_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
        orig_name = lastname_field.get_attribute("maxlength")
        print(orig_name)
        last_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_last_name = len(last_name)
        print(length_of_last_name)
        lastname_field.send_keys(last_name)
        time.sleep(3)
        length_result = lastname_field.get_attribute("value")
        final_result1 = len(length_result)
        print(length_of_last_name, final_result1)
        if final_result1 == 50:
            print("test_TC_018_18 pass")
        else:
            print("test_TC_018_18 fail")

    def test_TC_019_19(self):
        driver = self.driver
        print("negative TC_019_19")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        firstname_input = driver.find_element(By.XPATH, "//input[contains(@name,'firstName')]")
        invalid_name = "398392Q!@3"
        firstname_input.clear()
        firstname_input.send_keys(invalid_name)
        firstname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_019_19 fail. No error message when input incorrect symbols in "First name" field.')
        else:
            print('test_TC_019_19 pass. Error message "Invalid name" is right under "First name" field.')

    def test_TC_020_20(self):
        driver = self.driver
        print("negative TC_020_20")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        invalid_name = "qWA!#@#@!!8183881"
        lastname_input.clear()
        lastname_input.send_keys(invalid_name)
        lastname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_020_20 fail. No error message when input incorrect symbols in "Last name" field.')
        else:
            print('test_TC_020_20 pass. Error message "Invalid name" is right under "Last name" field.')

class FirefoxPositiveNegativeTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_016(self):
        driver = self.driver
        print("positive TC-016")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        if driver.title == "Model X | Tesla":
            print("TC-016 pass. Model X page is open correctly")
        else:
            print("TC-016 fail")
        driver.quit()

    def test_TC_017(self, current_url=None):
        driver = self.driver
        print("positive TC-017")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//label[contains(@for,'PR01')]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Six Seat Interior')]").click()
        delay()
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Order Now')]")
            if element:
                print("TC-017 pass. The users can customize their vehicle.")
            else:
                print("TC-017 fail. The users can't customize their vehicle.")
        except NoSuchElementException:
            print("TC-017 fail.")
        driver.quit()

    def test_TC_018(self):
        driver = self.driver
        print("positive TC-018")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']").click()
        time.sleep(6)
        try:
            shop_now = driver.find_element(By.XPATH, "//a[contains(@aria-describedby,'hero-0')]")
            if shop_now:
                print('TC-18 pass. "Shop now" button clickable.')
            else:
                print('TC-18 fail. "Shop now" button unclickable.')
        except NoSuchElementException:
                print("TC-18 fail.")
        driver.quit()

    def test_TC_019(self):
        driver = self.driver
        print("positive TC-019")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        try:
            element = driver.find_element(By.XPATH, "(//a[contains(@title,'Help Me Choose')])[1]")
            if element:
                print('TC-019 pass. "Compare Models" page loads correctly with all elements visible.')
            else:
                print('TC-019 fail. "Compare Models" page does not loads correctly.')
        except NoSuchElementException:
            print("TC-019 fail.")
        driver.quit()

    def test_TC_020(self):
        driver = self.driver
        print("positive TC-020")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,6000)")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@href='/compare'])[2]").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        try:
            element = driver.find_element(By.XPATH, "//button[contains(.,'Add Model')]")
            if element:
                print('TC-020 pass. Customer can compare Tesla Models')
            else:
                print('TC-020 fail. Customer can not compare Tesla Models')
        except NoSuchElementException:
            print("TC-020 fail.")
        driver.quit()

    def test_TC_016_16(self):
        driver = self.driver
        print("negative TC_016_16")
        driver.get("https://www.tesla.com/modelx/qwerty")
        error_code = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[1]')
        error_text = driver.find_element(By.XPATH, '//*[@id="article_content"]/div/div/div/div[2]')
        if error_code and error_text:
            print('"404" and page not found message is visible. Test pass.')
        else:
            print("No error message. test fail")
        driver.quit()

    def test_TC_017_17(self, current_url=None):
        driver = self.driver
        print("negative TC_017_17")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        firstname_field = driver.find_element(By.XPATH, '//*[@id="FIRST_NAME"]')
        orig_name = firstname_field.get_attribute("maxlength")
        print(orig_name)
        first_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_first_name = len(first_name)
        print(length_of_first_name)
        firstname_field.send_keys(first_name)
        time.sleep(3)
        length_result = firstname_field.get_attribute("value")
        final_result = len(length_result)
        print(length_of_first_name, final_result)
        if final_result == 50:
            print("test_TC_017_17 pass")
        else:
            print("test_TC_017_17 fail")
        driver.quit()

    def test_TC_018_18(self, current_url=None):
        driver = self.driver
        print("negative TC_018_18")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "(//a[contains(.,'Order Now')])[1]").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='Order with Card']").click()
        time.sleep(7)
        lastname_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
        orig_name = lastname_field.get_attribute("maxlength")
        print(orig_name)
        last_name = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        length_of_last_name = len(last_name)
        print(length_of_last_name)
        lastname_field.send_keys(last_name)
        time.sleep(3)
        length_result = lastname_field.get_attribute("value")
        final_result1 = len(length_result)
        print(length_of_last_name, final_result1)
        if final_result1 == 50:
            print("test_TC_018_18 pass")
        else:
            print("test_TC_018_18 fail")
        driver.quit()

    def test_TC_019_19(self):
        driver = self.driver
        print("negative TC_019_19")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        firstname_input = driver.find_element(By.XPATH, "//input[contains(@name,'firstName')]")
        invalid_name = "398392Q!@3"
        firstname_input.clear()
        firstname_input.send_keys(invalid_name)
        firstname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_019_19 fail. No error message when input incorrect symbols in "First name" field.')
        else:
            print('test_TC_019_19 pass. Error message "Invalid name" is right under "First name" field.')
        driver.quit()

    def test_TC_020_20(self):
        driver = self.driver
        print("negative TC_020_20")
        driver.get('https://www.tesla.com/')
        time.sleep(2)
        vehicles = (driver.find_element(By.XPATH, '//*[@id="dx-nav-item--vehicles"]'))
        actions = ActionChains(driver)
        actions.move_to_element(vehicles).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Model X']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@data-gtm-interaction='demo-drive']").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,1400)")
        time.sleep(3)
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        invalid_name = "qWA!#@#@!!8183881"
        lastname_input.clear()
        lastname_input.send_keys(invalid_name)
        lastname_input.send_keys(Keys.RETURN)
        error_message = None
        try:
            error_message = driver.find_element(By.CLASS_NAME, "Invalid name")
        except:
            pass
        if error_message is None:
            print('test_TC_020_20 fail. No error message when input incorrect symbols in "Last name" field.')
        else:
            print('test_TC_020_20 pass. Error message "Invalid name" is right under "Last name" field.')
        driver.quit()







