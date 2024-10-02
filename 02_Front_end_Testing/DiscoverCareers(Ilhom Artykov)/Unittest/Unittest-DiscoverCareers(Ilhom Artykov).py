from os import times_result, times
from re import search
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import WebDriverException as WDE


def delay():
    time.sleep(random.randint(1, 5))


class ChromePositiveTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService())
        self.driver.maximize_window()

    def test_case_011_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()

        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    def test_case_012_chrome(self):
        global new_window
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        print("Careers button is clickable")

    def tearDown(self):
            self.driver.quit()


    def test_case_013_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        print("Explore job is visible")

    def tearDown(self):
            self.driver.quit()


    def test_case_014_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        print("Explore job button is clickabe")

    def tearDown(self):
            self.driver.quit()


    def test_case_015_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='query']").click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='query']"))).send_keys("QA Tester")

    def tearDown(self):
            self.driver.quit()


class FirefoxPositiveTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=ChromeService())
        self.driver.maximize_window()

    def test_case_011_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()


    def tearDown(self):
        self.driver.quit()

    def test_case_012_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        print("Careers button is clickable")

    def tearDown(self):
            self.driver.quit()


    def test_case_013_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        print("Explore job is visible")

    def tearDown(self):
            self.driver.quit()


    def test_case_014_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        print("Explore job button is clickabe")

    def tearDown(self):
            self.driver.quit()


    def test_case_015_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='query']").click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='query']"))).send_keys("QA Tester")

    def tearDown(self):
            self.driver.quit()


class EdgePositiveTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=ChromeService())
        self.driver.maximize_window()

    def test_case_011_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()

        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    def test_case_012_edge(self):
        global new_window
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        print("Careers button is clickable")

    def tearDown(self):
            self.driver.quit()


    def test_case_013_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        print("Explore job is visible")

    def tearDown(self):
            self.driver.quit()


    def test_case_014_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        print("Explore job button is clickabe")

    def tearDown(self):
            self.driver.quit()


    def test_case_015_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]")
        driver.find_element(By.XPATH, "//span[contains(.,'Explore Jobs')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='query']").click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='query']"))).send_keys("QA Tester")

    def tearDown(self):
            self.driver.quit()


class ChromeNegativeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService())
        self.driver.maximize_window()

    def test_case_N011_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()

        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    def test_case_N012_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']")
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Must")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(1)
    def tearDown(self):
        self.driver.quit()


    def test_case_N013_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        driver.find_element(By.XPATH, "//input[@name='lastName']")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N014_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']")
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N015_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()



class FirefoxNegativeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=ChromeService())
        self.driver.maximize_window()

    def test_case_N011_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()

        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    def test_case_N012_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']")
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Must")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(1)
    def tearDown(self):
        self.driver.quit()


    def test_case_N013_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        driver.find_element(By.XPATH, "//input[@name='lastName']")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N014_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']")
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N015_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()



class EdgeNegativeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=ChromeService())
        self.driver.maximize_window()

    def test_case_N011_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()

        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    def test_case_N012_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']")
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Must")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(1)
    def tearDown(self):
        self.driver.quit()


    def test_case_N013_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        driver.find_element(By.XPATH, "//input[@name='lastName']")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N014_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']")
        driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("11235")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()


    def test_case_N015_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Discover')]"))).click()
        time.sleep(0.5)
        print("Discover button is visible")
        driver.find_element(By.XPATH, "(//a[@href='/careers'])[1]").click()
        time.sleep(1.5)
        try:
            assert "https://www.tesla.com/careers" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").is_displayed()
        driver.find_element(By.XPATH, "//a[contains(text(),'Get Updates')]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Ilon")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Musk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ilhomartykov@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='zip']")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    def tearDown(self):
        self.driver.quit()
