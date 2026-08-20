from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def delay():
    time.sleep(random.randint(1, 5))


class FirefoxPositiveTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # ------------------------------------------------------------------
    # BR137-P: Verify that "Shop" button clickable in the main page
    #          and transfer to correct page.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br137_p_shop_button_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')

        wait = WebDriverWait(driver, 10)
        # Verify Shop button is visible and clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/" in driver.current_url
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR138-P: Verify that "Apparel" button in shop menu clickable
    #          and transfer to correct page.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br138_p_apparel_button_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR139-P: Verify that button "Cybercab Trucker Hat" clickable
    #          and transfer to correct page.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Select and click the "Cybercab Trucker Hat"
    #   5. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br139_p_cybercab_trucker_hat_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Scrolling down to Cybercab Trucker Hat
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Cybercab Trucker Hat is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]").click()
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybercab-trucker-hat" in driver.current_url
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR140-P: Verify that "Search Line" work and transfer to correct page.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Click on the button "Search"
    #   5. Enter word "Hat"
    #   6. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br140_p_search_line_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is clickable")
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]").click()
        time.sleep(2)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='search']")))
        print("Search input is visible")
        search_input.click()
        time.sleep(1)
        search_input.send_keys("Hat")
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=Hat" in driver.current_url
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR141-P: Verify that button "Cybercab Trucker Hat" clickable
    #          and transfer to correct page.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Click on the button "Search"
    #   5. Enter word "Hat"
    #   6. Select and click the "Cybercab Trucker Hat"
    #   7. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br141_p_search_and_cybercab_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is clickable")
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]").click()
        time.sleep(2)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='search']")))
        print("Search input is visible")
        search_input.click()
        time.sleep(1)
        search_input.send_keys("Hat")
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=Hat" in driver.current_url
        print("Search URL is OK")
        time.sleep(2)

        # Verify Cybercab Trucker Hat is clickable from search results
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]").click()
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.tesla.com/product/cybercab-trucker-hat" in driver.current_url
        print("URL is OK")


class FirefoxNegativeTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # ------------------------------------------------------------------
    # BR137-N: Verify that user can added wrong information in Search Line.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Click on the button "Search"
    #   5. Enter "!!!" in Search Line
    #   6. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br137_n_search_wrong_info_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is clickable")
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]").click()
        time.sleep(2)

        # Verify Search Line added wrong keys
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='search']")))
        print("Search input is visible")
        search_input.click()
        time.sleep(1)
        search_input.send_keys("!!!")
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=!!!" in driver.current_url
        print("No Results Found")

    # ------------------------------------------------------------------
    # BR138-N: Verify that user CANNOT add "0" item to shopping cart.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Select and click the "Cybercab Trucker Hat"
    #   5. Choose quantity "0"
    #   6. Click "ADD TO CART"
    #   7. Make sure this item added to cart.
    # Expected: User can't buy "0" quantity item.
    # ------------------------------------------------------------------
    def test_br138_n_add_zero_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Scrolling down to Cybercab Trucker Hat
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Cybercab Trucker Hat is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]")))
        print("Cybercab Trucker Hat button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]").click()
        time.sleep(2)

        # Verify quantity "0" added
        qty = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='number']")))
        qty.click()
        qty.clear()
        qty.send_keys('0')
        time.sleep(2)

        # Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        driver.find_element(By.XPATH, "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(3)

        # --- Negative assertion: open cart and verify qty is NOT 0 ---
        driver.get("https://shop.tesla.com/cart")
        time.sleep(3)

        try:
            qty_in_cart = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='number']")))
            actual_qty = qty_in_cart.get_attribute('value')
        except TimeoutException:
            print("PASS: Cart is empty, 0 quantity was rejected")
            return

        assert actual_qty != '0', f"FAIL: Cart contains 0 quantity (actual: {actual_qty})"
        assert int(actual_qty) >= 1, f"FAIL: Unexpected quantity in cart: {actual_qty}"
        print(f"PASS: User can't buy 0 quantity item. System auto-set to: {actual_qty}")

    # ------------------------------------------------------------------
    # BR139-N: Verify that user can added wrong information in Search Line.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Click on the button "Search"
    #   5. Enter "12345" in Search Line
    #   6. Make sure it is transfer to correct page.
    # ------------------------------------------------------------------
    def test_br139_n_search_12345_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]")))
        print("Search button is clickable")
        driver.find_element(By.XPATH,
                            "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]").click()
        time.sleep(2)

        # Verify Search Line added wrong keys
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='search']")))
        print("Search input is visible")
        search_input.click()
        time.sleep(1)
        search_input.send_keys("12345")
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        assert "https://shop.tesla.com/search?searchTerm=12345" in driver.current_url
        print("No Results Found")

    # ------------------------------------------------------------------
    # BR140-N: Verify that user can't buy 0.5 quantity item.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Select and click the "Tesla Electric Summer Tee"
    #   5. Choose quantity "0.5"
    #   6. Click "ADD TO CART"
    #   7. Make sure this item added to cart.
    # Expected: User can't buy 0.5 quantity item.
    # ------------------------------------------------------------------
    def test_br140_n_buy_half_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Scrolling down to Tesla Optimus Code Tee
        driver.execute_script("window.scrollTo(0,700)")
        delay()

        # Verify Tesla Optimus Code Tee is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Tesla Optimus Code Tee')]")))
        print("Tesla Optimus Code Tee button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Tesla Optimus Code Tee')]")))
        print("Tesla Optimus Code Tee button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Tesla Optimus Code Tee')]").click()
        time.sleep(2)

        # Verify quantity "0.5" added
        qty = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='number']")))
        qty.click()
        qty.clear()
        qty.send_keys('0.5')
        time.sleep(2)

        # Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        driver.find_element(By.XPATH, "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(3)

        # --- Negative assertion: open cart and verify qty is NOT 0.5 ---
        driver.get("https://shop.tesla.com/cart")
        time.sleep(3)

        try:
            qty_in_cart = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='number']")))
            actual_qty = qty_in_cart.get_attribute('value')
        except TimeoutException:
            print("PASS: Cart is empty, 0.5 quantity was rejected")
            return

        assert actual_qty != '0.5', f"FAIL: Cart contains 0.5 quantity (actual: {actual_qty})"
        try:
            float_qty = float(actual_qty)
            assert float_qty >= 1, f"FAIL: Invalid quantity in cart: {actual_qty}"
        except ValueError:
            pass
        print(f"PASS: User can't buy 0.5 quantity item. System auto-set to: {actual_qty}")

    # ------------------------------------------------------------------
    # BR141-N: Verify that user can't buy 6 quantity item.
    # Steps:
    #   1. Enter https://www.tesla.com/
    #   2. Click on the button "Shop" on the header menu.
    #   3. Click on the button "Apparel"
    #   4. Select and click the "Tesla Core Hoodie"
    #   5. Choose quantity "6"
    #   6. Click "ADD TO CART"
    #   7. Make sure this item added to cart.
    # Expected: User can't buy 6 quantity item.
    # ------------------------------------------------------------------
    def test_br141_n_buy_six_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        wait = WebDriverWait(driver, 10)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]").click()
        time.sleep(2)

        # Verify Apparel button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Apparel')]")))
        print("Apparel button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Apparel')]").click()
        time.sleep(2)

        # Verify correct URL for Apparel
        assert "https://shop.tesla.com/category/apparel" in driver.current_url
        print("Apparel URL is OK")
        time.sleep(2)

        # Scrolling down to Tesla Core Hoodie
        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)

        # Verify Tesla Core Hoodie is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(.,'Tesla Core Hoodie')]")))
        print("Tesla Core Hoodie button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Tesla Core Hoodie')]")))
        print("Tesla Core Hoodie button is clickable")
        driver.find_element(By.XPATH, "//a[contains(.,'Tesla Core Hoodie')]").click()
        time.sleep(2)

        # Verify quantity "6" added
        qty = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='number']")))
        qty.click()
        qty.clear()
        qty.send_keys('6')
        time.sleep(2)

        # Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id,'addToCartBtn')]")))
        print("Add to cart button is clickable")
        driver.find_element(By.XPATH, "//input[contains(@id,'addToCartBtn')]").click()
        time.sleep(3)

        # --- Negative assertion: open cart and verify qty is NOT 6 ---
        driver.get("https://shop.tesla.com/cart")
        time.sleep(3)

        try:
            qty_in_cart = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='number']")))
            actual_qty = qty_in_cart.get_attribute('value')
        except TimeoutException:
            print("PASS: Cart is empty, 6 quantity was rejected")
            return

        assert actual_qty != '6', f"FAIL: Cart contains 6 quantity (actual: {actual_qty})"
        assert int(actual_qty) <= 5, f"FAIL: Quantity exceeds max allowed: {actual_qty}"
        print(f"PASS: User can't buy 6 quantity item. System auto-set to: {actual_qty}")


if __name__ == "__main__":
    unittest.main()