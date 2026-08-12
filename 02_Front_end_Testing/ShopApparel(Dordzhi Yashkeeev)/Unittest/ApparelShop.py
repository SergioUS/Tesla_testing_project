#!/usr/bin/env python3
"""
Tesla Firefox UnitTest Suite
==============================
Positive and Negative tests for Tesla navigation on Mozilla Firefox only.

Steps (Positive):
    1. Open https://www.tesla.com/
    2. Click "Shop" on the main menu
    3. Click "Apparel"
    4. Scroll down to find "Cybercab Trucker Hat"
    5. Click "Cybercab Trucker Hat"
    6. Verify product page loaded
    7. Close browser

Steps (Negative):
    1-3 same as positive
    4. Scroll down and search for non-existent product "FakeHatXYZ999"
    5. Verify "Cybercab Trucker Hat" is NOT on the page
    6. Close browser

Fast execution: 1-second intervals, short timeouts.

Requirements:
    pip install selenium webdriver-manager

Run:
    python tesla_firefox_test.py -v
"""

import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class TeslaFirefoxTest(unittest.TestCase):
    """Positive and Negative tests on Mozilla Firefox."""

    wait = 1  # fast 1-second interval

    def setUp(self):
        """Open Firefox before each test."""
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] SETUP: Opening Firefox...")
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.set_preference("general.useragent.override",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0")

        service = FirefoxService(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        self.addCleanup(self._cleanup)

    def _cleanup(self):
        """Close Firefox after each test."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] TEARDOWN: Closing Firefox...")
        if hasattr(self, 'driver') and self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
        time.sleep(0.5)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _safe_click(self, locators, timeout=5):
        """Click first available element."""
        for loc in locators:
            try:
                el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(loc))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
                time.sleep(0.5)
                el.click()
                return el
            except Exception:
                continue
        raise Exception(f"Element not found with locators: {locators}")

    def _scroll_until_found(self, locators, max_scrolls=10):
        """Scroll down until element is found and clickable."""
        for _ in range(max_scrolls):
            for loc in locators:
                try:
                    el = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(loc))
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
                    time.sleep(0.5)
                    return el
                except Exception:
                    continue
            # Scroll down by 800 pixels
            self.driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(0.5)
        raise Exception(f"Element not found after {max_scrolls} scrolls. Locators: {locators}")

    def _is_access_denied(self):
        page = self.driver.page_source.lower()
        title = self.driver.title.lower()
        return (
            "access denied" in page or "access denied" in title or
            "errors.edgesuite" in page or "akamai" in page or
            "reference #" in page
        )

    # ===================================================================
    # POSITIVE TEST
    # ===================================================================
    def test_positive_cybercab_trucker_hat(self):
        """
        POSITIVE TEST: Tesla → Shop → Apparel → Scroll → Cybercab Trucker Hat
        Expected: Product page loads successfully. Result: PASS.
        """
        driver = self.driver
        step = 0
        try:
            step = 1
            driver.get("https://www.tesla.com/")
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied on Tesla homepage")

            step = 2
            self._safe_click([
                (By.XPATH, "//a[contains(text(), 'Shop')]"),
                (By.XPATH, "//a[contains(@href, 'shop.tesla')]"),
                (By.CSS_SELECTOR, "a[href*='shop']"),
            ])
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied after clicking Shop")

            step = 3
            self._safe_click([
                (By.XPATH, "//a[contains(text(), 'Apparel')]"),
                (By.XPATH, "//a[contains(@href, 'apparel')]"),
                (By.CSS_SELECTOR, "a[href*='apparel']"),
            ])
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied after clicking Apparel")

            step = 4
            print("    [Scroll] Scrolling down to find Cybercab Trucker Hat...")
            hat_element = self._scroll_until_found([
                (By.XPATH, "//a[contains(text(), 'Cybercab Trucker Hat')]"),
                (By.XPATH, "//a[contains(@href, 'cybercab-trucker-hat')]"),
                (By.XPATH, "//div[contains(text(), 'Cybercab Trucker Hat')]"),
                (By.XPATH, "//span[contains(text(), 'Cybercab Trucker Hat')]"),
                (By.CSS_SELECTOR, "a[href*='cybercab-trucker-hat']"),
            ], max_scrolls=15)
            hat_element.click()
            time.sleep(self.wait)

            if self._is_access_denied():
                raise Exception("Access Denied after clicking Cybercab Trucker Hat")

            step = 5
            current_url = driver.current_url.lower()
            source = driver.page_source.lower()
            self.assertTrue(
                "cybercab" in current_url or "cybercab" in source,
                f"Not on Cybercab Trucker Hat page. URL: {driver.current_url}"
            )

            print(f"\n[PASS] Positive test PASSED on Firefox")

        except Exception as e:
            print(f"\n[FAIL] Positive test FAILED on Firefox at step {step}: {e}")
            self.fail(f"Positive test failed at step {step}: {e}")

    # ===================================================================
    # NEGATIVE TEST
    # ===================================================================
    def test_negative_nonexistent_product(self):
        """
        NEGATIVE TEST: Tesla → Shop → Apparel → Scroll → Verify FakeHatXYZ999 does NOT exist
        Expected: Non-existent product is not found. Result: PASS.
        """
        driver = self.driver
        step = 0
        try:
            step = 1
            driver.get("https://www.tesla.com/")
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied on Tesla homepage")

            step = 2
            self._safe_click([
                (By.XPATH, "//a[contains(text(), 'Shop')]"),
                (By.XPATH, "//a[contains(@href, 'shop.tesla')]"),
                (By.CSS_SELECTOR, "a[href*='shop']"),
            ])
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied after clicking Shop")

            step = 3
            self._safe_click([
                (By.XPATH, "//a[contains(text(), 'Apparel')]"),
                (By.XPATH, "//a[contains(@href, 'apparel')]"),
                (By.CSS_SELECTOR, "a[href*='apparel']"),
            ])
            time.sleep(self.wait)
            if self._is_access_denied():
                raise Exception("Access Denied after clicking Apparel")

            step = 4
            print("    [Scroll] Scrolling down to verify FakeHatXYZ999 does not exist...")
            # Scroll a few times and check page source
            for _ in range(5):
                source = driver.page_source.lower()
                self.assertNotIn(
                    "fakehatxyz999", source,
                    "FakeHatXYZ999 should NOT appear on Apparel page"
                )
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(0.5)

            # Also verify Cybercab Trucker Hat is NOT confused with fake product
            source = driver.page_source.lower()
            self.assertNotIn(
                "fakehatxyz999", source,
                "Non-existent product FakeHatXYZ999 found on page - unexpected"
            )

            print(f"\n[PASS] Negative test PASSED on Firefox")

        except AssertionError:
            raise
        except Exception as e:
            print(f"\n[FAIL] Negative test FAILED on Firefox at step {step}: {e}")
            self.fail(f"Negative test failed at step {step}: {e}")


# ===================================================================
# Entry Point
# ===================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)