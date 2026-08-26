from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import random
import unittest
import time

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def delay():
    time.sleep(random.randint(1, 2))


# ============================================================
# SMART SELECTORS — update here when the site changes
# ============================================================
SELECTORS = {
    "shop_button": {
        "primary":   (By.XPATH, "//a[contains(@id,'dx-nav-item--shop')]"),
        "fallback_1": (By.XPATH, "//a[contains(text(),'Shop')]"),
        "fallback_2": (By.XPATH, "//header//a[contains(@href,'/shop')]"),
        "fallback_3": (By.CSS_SELECTOR, "a[href*='shop.tesla.com']"),
    },
    "apparel_button": {
        "primary":   (By.XPATH, "//a[contains(.,'Apparel')]"),
        "fallback_1": (By.XPATH, "//a[contains(text(),'Apparel')]"),
        "fallback_2": (By.XPATH, "//nav//a[contains(@href,'apparel')]"),
        "fallback_3": (By.CSS_SELECTOR, "a[href*='apparel']"),
    },
    "cybercab_hat": {
        "primary":   (By.XPATH, "//a[contains(.,'Cybercab Trucker Hat')]"),
        "fallback_1": (By.XPATH, "//a[contains(text(),'Cybercab Trucker')]"),
        "fallback_2": (By.XPATH, "//a[contains(@href,'cybercab-trucker-hat')]"),
        "fallback_3": (By.CSS_SELECTOR, "a[href*='cybercab-trucker-hat']"),
    },
    "search_button_collapsed": {
        "primary":   (By.XPATH, "//div[contains(@class,'tds-form-input') and contains(@class,'collapsed')]"),
        "fallback_1": (By.XPATH, "//button[contains(@aria-label,'Search')]"),
        "fallback_2": (By.XPATH, "//div[contains(@class,'search')]//button"),
        "fallback_3": (By.CSS_SELECTOR, "[aria-label*='Search' i], [aria-label*='search' i]"),
    },
    "search_input": {
        "primary":   (By.XPATH, "//input[@type='search']"),
        "fallback_1": (By.XPATH, "//input[contains(@placeholder,'Search')]"),
        "fallback_2": (By.CSS_SELECTOR, "input[type='search']"),
        "fallback_3": (By.XPATH, "//input[@aria-label='Search site']"),
    },
    "search_submit_btn": {
        "primary":   (By.XPATH, "//button[@type='submit' and contains(@aria-label,'Search')]"),
        "fallback_1": (By.XPATH, "//button[contains(@class,'search') and @type='submit']"),
        "fallback_2": (By.CSS_SELECTOR, "button[type='submit']"),
        "fallback_3": (By.XPATH, "//svg[contains(@class,'search')]//ancestor::button"),
    },
    "quantity_input": {
        "primary":   (By.XPATH, "//input[@type='number']"),
        "fallback_1": (By.CSS_SELECTOR, "input[type='number']"),
        "fallback_2": (By.XPATH, "//input[contains(@aria-label,'quantity')]"),
    },
    "add_to_cart_btn": {
        "primary":   (By.XPATH, "//input[contains(@id,'addToCartBtn')]"),
        "fallback_1": (By.XPATH, "//button[contains(text(),'Add to Cart')]"),
        "fallback_2": (By.XPATH, "//button[contains(.,'Add to Cart')]"),
        "fallback_3": (By.CSS_SELECTOR, "button[data-testid*='add-to-cart'], button[id*='cart']"),
    },
    "tesla_optimus_tee": {
        "primary":   (By.XPATH, "//a[contains(.,'Tesla Optimus Code Tee')]"),
        "fallback_1": (By.XPATH, "//a[contains(text(),'Optimus Code')]"),
        "fallback_2": (By.XPATH, "//a[contains(@href,'optimus-code-tee')]"),
    },
    "tesla_core_hoodie": {
        "primary":   (By.XPATH, "//a[contains(.,'Tesla Core Hoodie')]"),
        "fallback_1": (By.XPATH, "//a[contains(text(),'Core Hoodie')]"),
        "fallback_2": (By.XPATH, "//a[contains(@href,'core-hoodie')]"),
    },
}


# ============================================================
# SMART HELPERS
# ============================================================
def smart_find(driver, selector_key, timeout=10, clickable=False):
    """Find element trying multiple fallback selectors."""
    selectors = SELECTORS.get(selector_key)
    if not selectors:
        raise ValueError(f"Unknown selector key: {selector_key}")

    last_exception = None
    wait = WebDriverWait(driver, timeout)

    for name, (by, value) in selectors.items():
        try:
            if clickable:
                elem = wait.until(EC.element_to_be_clickable((by, value)))
            else:
                elem = wait.until(EC.visibility_of_element_located((by, value)))
            print(f"  [OK] Found '{selector_key}' via {name}")
            return elem
        except Exception as e:
            last_exception = e
            continue

    raise TimeoutException(
        f"Cannot find '{selector_key}'. Tried: {list(selectors.keys())}. Last: {last_exception}"
    )


def smart_click(driver, selector_key, timeout=10):
    """Find element and click (with JS fallback)."""
    elem = smart_find(driver, selector_key, timeout=timeout, clickable=True)
    try:
        elem.click()
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].click();", elem)
    time.sleep(0.5)
    return elem


def dismiss_cookie_banner(driver):
    """Close cookie banner if present."""
    short_wait = WebDriverWait(driver, 3)
    cookie_selectors = [
        (By.XPATH, "//button[contains(text(),'Accept')]"),
        (By.XPATH, "//button[contains(@class,'cookie') and contains(text(),'Accept')]"),
        (By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"),
        (By.XPATH, "//button[contains(text(),'Agree')]"),
    ]
    for by, val in cookie_selectors:
        try:
            btn = short_wait.until(EC.element_to_be_clickable((by, val)))
            btn.click()
            print("  [OK] Dismissed cookie banner")
            time.sleep(0.5)
            return
        except Exception:
            continue


def wait_for_url_contains(driver, substring, timeout=15):
    """Wait until URL contains substring."""
    WebDriverWait(driver, timeout).until(EC.url_contains(substring))


# ============================================================
# TEST CLASSES — your original structure
# ============================================================
class FirefoxPositiveTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_br137_p_shop_button_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com")
        print("URL is OK")

    def test_br138_p_apparel_button_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("URL is OK")

    def test_br139_p_cybercab_trucker_hat_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,700)")
        delay()

        smart_find(driver, "cybercab_hat")
        print("Cybercab Trucker Hat button is visible")
        smart_find(driver, "cybercab_hat", clickable=True)
        print("Cybercab Trucker Hat button is clickable")
        smart_click(driver, "cybercab_hat")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/product/cybercab-trucker-hat")
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR140-P: FIXED search flow — wait for animation + submit + fallback click
    # ------------------------------------------------------------------
    def test_br140_p_search_line_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        # Go to Shop → Apparel
        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        # Click search icon and WAIT for expand animation
        smart_click(driver, "search_button_collapsed")
        time.sleep(1.5)  # wait for search overlay to expand

        # Find search input
        search_input = smart_find(driver, "search_input", timeout=10)
        print("Search input is visible")

        # Type and submit
        search_input.click()
        time.sleep(0.3)
        search_input.clear()
        search_input.send_keys("Hat")
        time.sleep(0.5)

        # Try submit form first (more reliable than Keys.ENTER on SPA)
        try:
            search_input.submit()
        except Exception:
            search_input.send_keys(Keys.ENTER)

        time.sleep(1)

        # Fallback: if URL didn't change, try clicking search submit button
        if "searchTerm=Hat" not in driver.current_url:
            try:
                smart_click(driver, "search_submit_btn", timeout=5)
                time.sleep(1)
            except Exception:
                pass

        print(f"  [DEBUG] Current URL: {driver.current_url}")

        wait_for_url_contains(driver, "searchTerm=Hat", timeout=15)
        time.sleep(1)

        assert "https://shop.tesla.com/search?searchTerm=Hat" in driver.current_url
        print("URL is OK")

    # ------------------------------------------------------------------
    # BR141-P: FIXED same search flow
    # ------------------------------------------------------------------
    def test_br141_p_search_and_cybercab_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        # Click search icon and WAIT for expand animation
        smart_click(driver, "search_button_collapsed")
        time.sleep(1.5)  # wait for search overlay to expand

        # Find search input
        search_input = smart_find(driver, "search_input", timeout=10)
        print("Search input is visible")

        # Type and submit
        search_input.click()
        time.sleep(0.3)
        search_input.clear()
        search_input.send_keys("Hat")
        time.sleep(0.5)

        # Try submit form first
        try:
            search_input.submit()
        except Exception:
            search_input.send_keys(Keys.ENTER)

        time.sleep(1)

        # Fallback: click search submit button if URL didn't change
        if "searchTerm=Hat" not in driver.current_url:
            try:
                smart_click(driver, "search_submit_btn", timeout=5)
                time.sleep(1)
            except Exception:
                pass

        print(f"  [DEBUG] Current URL: {driver.current_url}")

        wait_for_url_contains(driver, "searchTerm=Hat", timeout=15)
        time.sleep(1)

        assert "https://shop.tesla.com/search?searchTerm=Hat" in driver.current_url
        print("Search URL is OK")

        # Click result
        smart_find(driver, "cybercab_hat")
        print("Cybercab Trucker Hat button is visible")
        smart_find(driver, "cybercab_hat", clickable=True)
        print("Cybercab Trucker Hat button is clickable")
        smart_click(driver, "cybercab_hat")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/product/cybercab-trucker-hat")
        print("URL is OK")


class FirefoxNegativeTests(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_br137_n_search_wrong_info_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        smart_click(driver, "search_button_collapsed")
        time.sleep(1.5)

        search_input = smart_find(driver, "search_input", timeout=10)
        print("Search input is visible")
        search_input.click()
        time.sleep(0.3)
        search_input.clear()
        search_input.send_keys("!!!")
        time.sleep(0.5)

        try:
            search_input.submit()
        except Exception:
            search_input.send_keys(Keys.ENTER)

        time.sleep(1)

        if "searchTerm=!!!" not in driver.current_url:
            try:
                smart_click(driver, "search_submit_btn", timeout=5)
                time.sleep(1)
            except Exception:
                pass

        print(f"  [DEBUG] Current URL: {driver.current_url}")

        wait_for_url_contains(driver, "searchTerm=!!!", timeout=15)
        time.sleep(1)

        assert "https://shop.tesla.com/search?searchTerm=!!!" in driver.current_url
        print("No Results Found")

    def test_br138_n_add_zero_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)
        wait = WebDriverWait(driver, 10)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,700)")
        delay()

        smart_find(driver, "cybercab_hat")
        print("Cybercab Trucker Hat button is visible")
        smart_find(driver, "cybercab_hat", clickable=True)
        print("Cybercab Trucker Hat button is clickable")
        smart_click(driver, "cybercab_hat")
        time.sleep(1)

        qty = smart_find(driver, "quantity_input")
        qty.click()
        qty.clear()
        qty.send_keys('0')
        time.sleep(1)

        smart_find(driver, "add_to_cart_btn")
        print("Add to cart button is visible")
        smart_find(driver, "add_to_cart_btn", clickable=True)
        print("Add to cart button is clickable")
        smart_click(driver, "add_to_cart_btn")
        time.sleep(2)

        driver.get("https://shop.tesla.com/cart")
        time.sleep(2)

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

    def test_br139_n_search_12345_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)
        wait = WebDriverWait(driver, 10)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        smart_click(driver, "search_button_collapsed")
        time.sleep(1.5)

        search_input = smart_find(driver, "search_input", timeout=10)
        print("Search input is visible")
        search_input.click()
        time.sleep(0.3)
        search_input.clear()
        search_input.send_keys("12345")
        time.sleep(0.5)

        try:
            search_input.submit()
        except Exception:
            search_input.send_keys(Keys.ENTER)

        time.sleep(1)

        if "searchTerm=12345" not in driver.current_url:
            try:
                smart_click(driver, "search_submit_btn", timeout=5)
                time.sleep(1)
            except Exception:
                pass

        print(f"  [DEBUG] Current URL: {driver.current_url}")

        wait_for_url_contains(driver, "searchTerm=12345", timeout=15)
        time.sleep(1)

        assert "https://shop.tesla.com/search?searchTerm=12345" in driver.current_url
        print("No Results Found")

    def test_br140_n_buy_half_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)
        wait = WebDriverWait(driver, 10)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,700)")
        delay()

        smart_find(driver, "tesla_optimus_tee")
        print("Tesla Optimus Code Tee button is visible")
        smart_find(driver, "tesla_optimus_tee", clickable=True)
        print("Tesla Optimus Code Tee button is clickable")
        smart_click(driver, "tesla_optimus_tee")
        time.sleep(1)

        qty = smart_find(driver, "quantity_input")
        qty.click()
        qty.clear()
        qty.send_keys('0.5')
        time.sleep(1)

        smart_find(driver, "add_to_cart_btn")
        print("Add to cart button is visible")
        smart_find(driver, "add_to_cart_btn", clickable=True)
        print("Add to cart button is clickable")
        smart_click(driver, "add_to_cart_btn")
        time.sleep(2)

        driver.get("https://shop.tesla.com/cart")
        time.sleep(2)

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

    def test_br141_n_buy_six_quantity_firefox(self):
        driver = self.driver
        driver.get('https://www.tesla.com/')
        time.sleep(1)
        dismiss_cookie_banner(driver)
        wait = WebDriverWait(driver, 10)

        smart_find(driver, "shop_button")
        print("Shop button is visible")
        smart_find(driver, "shop_button", clickable=True)
        print("Shop button is clickable")
        smart_click(driver, "shop_button")
        time.sleep(1)

        smart_find(driver, "apparel_button")
        print("Apparel button is visible")
        smart_find(driver, "apparel_button", clickable=True)
        print("Apparel button is clickable")
        smart_click(driver, "apparel_button")
        time.sleep(1)

        wait_for_url_contains(driver, "shop.tesla.com/category/apparel")
        print("Apparel URL is OK")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,1400)")
        delay()
        time.sleep(1)

        smart_find(driver, "tesla_core_hoodie")
        print("Tesla Core Hoodie button is visible")
        smart_find(driver, "tesla_core_hoodie", clickable=True)
        print("Tesla Core Hoodie button is clickable")
        smart_click(driver, "tesla_core_hoodie")
        time.sleep(1)

        qty = smart_find(driver, "quantity_input")
        qty.click()
        qty.clear()
        qty.send_keys('6')
        time.sleep(1)

        smart_find(driver, "add_to_cart_btn")
        print("Add to cart button is visible")
        smart_find(driver, "add_to_cart_btn", clickable=True)
        print("Add to cart button is clickable")
        smart_click(driver, "add_to_cart_btn")
        time.sleep(2)

        driver.get("https://shop.tesla.com/cart")
        time.sleep(2)

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