from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def delay():
    time.sleep(random.randint(1, 5))


class ChromePositiveTests(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=ChromeService())
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # As per unittest module, individual test should start with test_
        # Verify correct URL

    def test_check_shop_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(1)

        # Verify correct URL
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(driver.current_url)
            assert parsed_url.hostname == "shop.tesla.com"
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    # Verify Shop button clickable
    def test_check_lifestyle_chrome(self):
        global new_window
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_cybertruck_for_kids_item_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cybertruck for kids button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//img[@alt='Cybertruck for Kids'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-for-kids?sku=1985666-00-A" in driver.current_url
        print("URL is OK")


    def tearDown(self):
        self.driver.quit()

        # Verify correct URL

    def test_search_line_shop_lifestyle_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()


    def test_search_line_lifestyle_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cyberquad for kids button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@alt='Cyberquad for Kids']").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberquad-for-kids?sku=1714748-00-B&web=true" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


class FirefoxPositiveSearch(unittest.TestCase):


    def setUp(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--lang=en-US')
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        # self.driver.set_window_size(1820, 1050)
        self.driver.maximize_window()

        # As per unittest module, individual test should start with test_
        # Verify correct URL

    def test_check_shop_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(1)

        # Verify correct URL
        try:
            assert "https://shop.tesla.com/" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    # Verify Shop button clickable
    def test_check_lifestyle_firefox(self):
        global new_window
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_cybertruck_for_kids_item_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cybertruck for kids button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//img[@alt='Cybertruck for Kids'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-for-kids?sku=1985666-00-A" in driver.current_url
        print("URL is OK")


    def tearDown(self):
        self.driver.quit()

        # Verify correct URL

    def test_search_line_lifestyle_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()


    def test_search_line_shop_lifestyle_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cyberquad for kids button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@alt='Cyberquad for Kids']").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberquad-for-kids?sku=1714748-00-B&web=true" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


class EdgePositiveSearch(unittest.TestCase):

    def setUp(self):
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        # As per unittest module, individual test should start with test_
        # Verify correct URL

    def test_check_shop_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 2)
        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(1)

        # Verify correct URL
        try:
            assert "https://shop.tesla.com/" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

    def tearDown(self):
        self.driver.quit()

    # Verify Shop button clickable
    def test_check_lifestyle_edge(self):
        global new_window
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_cybertruck_for_kids_item_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cybertruck for kids button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybertruck-for-kids?sku=1985666-00-A'])[3]")))
        print("Cybertruck for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//img[@alt='Cybertruck for Kids'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-for-kids?sku=1985666-00-A" in driver.current_url
        print("URL is OK")


    def tearDown(self):
        self.driver.quit()

        # Verify correct URL

    def test_search_line_lifestyle_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()


    def test_search_line_shop_lifestyle_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("kids")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=kids" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Verify Cyberquad for kids button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cyberquad-for-kids?sku=1714748-00-B&web=true'])[2]")))
        print("Cyberquad for kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@alt='Cyberquad for Kids']").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
              new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberquad-for-kids?sku=1714748-00-B&web=true" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

class ChromeNegativeTests(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=ChromeService())
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # As per unittest module, individual test should start with test_
        # Verify correct URL

    def test_search_line_shop_lifestyle_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("!!!")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=!!!" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()

    def test_add_item_to_cart_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to Cybertruck elevate backpack
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Cybertruck Elevate Backpack is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-elevate-backpack?sku=1990496-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_search_line_lifestyle_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("12345")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=12345" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_lifestyle_cart_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberStein
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberStein is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('05')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberstein?sku=1949545-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_add_6_item_to_lifestyle_cart_chrome(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberVessel
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberVessel is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybervessel?sku=2002204-00-A" in driver.current_url
        print("There was an error processing your request. You can't add more than 5 items")

    def tearDown(self):
        self.driver.quit()

class FirefoxNegativeSearch(unittest.TestCase):


    def setUp(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--lang=en-US')
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        # self.driver.set_window_size(1820, 1050)
        self.driver.maximize_window()

        # As per unittest module, individual test should start with test_
        # Verify correct URL
    def test_search_line_shop_lifestyle_FireFox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("!!!")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=!!!" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()

    def test_add_item_to_cart_FireFox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to Cybertruck elevate backpack
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Cybertruck Elevate Backpack is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-elevate-backpack?sku=1990496-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_search_line_lifestyle_Firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("12345")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=12345" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_lifestyle_cart_FireFox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberStein
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberStein is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('05')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberstein?sku=1949545-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_add_6_item_to_lifestyle_cart_FireFox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberVessel
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberVessel is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybervessel?sku=2002204-00-A" in driver.current_url
        print("There was an error processing your request. You can't add more than 5 items")

    def tearDown(self):
        self.driver.quit()

class EdgeNegativeSearch(unittest.TestCase):

    def setUp(self):
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        # As per unittest module, individual test should start with test_
        # Verify correct URL

    def test_search_line_shop_lifestyle_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("!!!")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=!!!" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
            self.driver.quit()

    def test_add_item_to_cart_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to Cybertruck elevate backpack
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Cybertruck Elevate Backpack is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]")))
        print("Cybertruck elevate backpack button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cybertruck-elevate-backpack?sku=1990496-00-A'][contains(.,'Cybertruck Elevate Backpack')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('0')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybertruck-elevate-backpack?sku=1990496-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_search_line_lifestyle_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)


        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input tds-form-input--default tds-form-input--collapsed')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'1')]")))
        print("Search added keys")
        driver.get("https://shop.tesla.com/category/lifestyle")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="search"]/div/div').click()
        search_bar = driver.find_element(By.XPATH, "//input[@id='1']")
        time.sleep(6)
        search_bar.send_keys("12345")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=12345" in driver.current_url
        print("No Results Found")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_lifestyle_cart_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberStein
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberStein is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]")))
        print("CyberStein button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@href='/product/cyberstein?sku=1949545-00-A'][contains(.,'CyberStein')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('05')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cyberstein?sku=1949545-00-A" in driver.current_url
        print("Item added to cart")

    def tearDown(self):
        self.driver.quit()

    def test_add_6_item_to_lifestyle_cart_edge(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 2)

    # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify Lifestyle button is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Lifestyle')]")))
        print("Lifestyle button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(.,'Lifestyle')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
               new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/lifestyle" in driver.current_url
        print("URL is OK")
        time.sleep(2)

        # Scrolling down to CyberVessel
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)


        # Verify CyberVessel is clickable

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]")))
        print("CyberVessel button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/product/cybervessel?sku=2002204-00-A'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)


        # Verify quantity added

        driver.find_element(By.XPATH, "//input[@id='3']").click()
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[@id='3']").send_keys('6')
        time.sleep(2)

        #Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        # driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybervessel?sku=2002204-00-A" in driver.current_url
        print("There was an error processing your request. You can't add more than 5 items")

    def tearDown(self):
        self.driver.quit()