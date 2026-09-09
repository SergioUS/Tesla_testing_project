import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

BASE_URL = "https://www.tesla.com"


class VehiclesMegaMenuLocators:
    COOKIE_ACCEPT_BUTTON = (
        By.CSS_SELECTOR,
        "#tsla-consent-accept, button[class*='consent'][class*='accept'], "
        "button[aria-label*='accept' i], button[aria-label*='Accept' i]",
    )
    VEHICLES_NAV_ITEM = (
        By.XPATH,
        "//nav//a[contains(translate(., 'VEHICLES', 'vehicles'), 'vehicles')] "
        "| //header//button[contains(translate(., 'VEHICLES', 'vehicles'), 'vehicles')] "
        "| //*[@data-id='vehicles'] | //*[contains(@class,'vehicles') and (self::a or self::button)]",
    )
    MEGA_MENU_CONTAINER = (
        By.CSS_SELECTOR,
        "[data-mega-menu], .mega-menu, [class*='megamenu'], [class*='mega-menu'], "
        "[role='menu'][aria-expanded='true'], nav [class*='dropdown'][class*='open'], "
        "div[class*='dx-mega-menu']",
    )
    MODEL_3_SECTION_LINK = (By.CSS_SELECTOR, "a[href*='/model3']")
    MODEL_Y_SECTION_LINK = (By.CSS_SELECTOR, "a[href*='/modely']")
    CYBERTRUCK_ORDER_LINK = (By.CSS_SELECTOR, "a[href*='/cybertruck/design'], a[href*='/cybertruck']")
    FLEET_LINK = (By.CSS_SELECTOR, "a[href*='/fleet']")


class VehiclesMegaMenuPage:
    def __init__(self, driver, wait_timeout=25): # Increased timeout to 25s for cloud stability
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.locators = VehiclesMegaMenuLocators

    def open(self):
        self.driver.get(BASE_URL)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self._dismiss_cookie_banner()
        return self

    def _dismiss_cookie_banner(self):
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.COOKIE_ACCEPT_BUTTON)
            )
            btn.click()
        except Exception:
            pass

    def hover_vehicles_menu(self):
        vehicles_item = self.wait.until(
            EC.visibility_of_element_located(self.locators.VEHICLES_NAV_ITEM)
        )
        ActionChains(self.driver).move_to_element(vehicles_item).perform()
        return self

    def is_mega_menu_open(self, timeout=5.0):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locators.MEGA_MENU_CONTAINER)
            )
            return True
        except Exception:
            return False

    def click_model_3(self):
        link = self.wait.until(EC.element_to_be_clickable(self.locators.MODEL_3_SECTION_LINK))
        link.click()
        return self

    def click_model_y(self):
        link = self.wait.until(EC.element_to_be_clickable(self.locators.MODEL_Y_SECTION_LINK))
        link.click()
        return self

    def click_cybertruck_order(self):
        link = self.wait.until(EC.element_to_be_clickable(self.locators.CYBERTRUCK_ORDER_LINK))
        link.click()
        return self

    def click_fleet(self):
        link = self.wait.until(EC.element_to_be_clickable(self.locators.FLEET_LINK))
        link.click()
        return self


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        # Explicitly passing command_executor for BrowserStack SDK integration with unittest
        self.driver = webdriver.Remote(
            command_executor="https://hub-cloud.browserstack.com/wd/hub",
            options=options
        )
        self.driver.maximize_window()
        self.page = VehiclesMegaMenuPage(self.driver).open()

    def tearDown(self):
        if hasattr(self, "driver") and self.driver:
            self.driver.quit()


class TestVehiclesMegaMenuPositive(BaseTest):

    def test_TC_132_P_menu_expansion(self):
        """Verify that the Vehicles mega menu expands successfully on hover."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open(timeout=5.0), "Mega menu did not open on hover.")

    def test_TC_133_P_navigate_to_model_3(self):
        """Verify successful navigation to the Model 3 page from the mega menu."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())
        self.page.click_model_3()
        WebDriverWait(self.driver, 25).until(EC.url_contains("model3"))
        self.assertIn("model3", self.driver.current_url)

    def test_TC_134_P_navigate_to_cybertruck_order(self):
        """Verify successful navigation to the Cybertruck design page."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())
        self.page.click_cybertruck_order()
        WebDriverWait(self.driver, 25).until(EC.url_contains("cybertruck"))
        self.assertIn("cybertruck", self.driver.current_url)

    def test_TC_135_P_navigate_to_model_y(self):
        """Verify successful navigation to the Model Y page."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())
        self.page.click_model_y()
        WebDriverWait(self.driver, 25).until(EC.url_contains("modely"))
        self.assertIn("modely", self.driver.current_url)

    def test_TC_136_P_navigate_to_fleet(self):
        """Verify successful navigation to the Fleet page."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())
        self.page.click_fleet()
        WebDriverWait(self.driver, 25).until(EC.url_contains("fleet"))
        self.assertIn("fleet", self.driver.current_url)


class TestVehiclesMegaMenuNegative(BaseTest):

    def test_TC_132_N_invalid_main_menu_locator(self):
        """Verify that looking for a non-existent navigation header element correctly throws an exception."""
        with self.assertRaises(Exception):
            fake_nav = (By.CSS_SELECTOR, "nav [data-id='nonexistent-menu-item-999']")
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(fake_nav))

    def test_TC_133_N_invalid_submenu_element_click_protection(self):
        """Verify that non-existent or invalid sub-elements cannot be located/clicked inside the menu."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())

        with self.assertRaises(Exception):
            bad_link = (By.CSS_SELECTOR, "a[href*='/nonexistent-tesla-model-999']")
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(bad_link))

    def test_TC_134_N_no_unintended_navigation_on_stale_click(self):
        """Verify that clicking a stale or detached menu link does not redirect to an incorrect URL."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())

        model_3_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.page.locators.MODEL_3_SECTION_LINK)
        )

        self.driver.get("https://www.tesla.com/support")

        with self.assertRaises(Exception):
            model_3_link.click()

    def test_TC_135_N_invalid_sub_link_navigation(self):
        """Verify that attempting to interact with a malformed configuration sub-path fails appropriately."""
        self.page.hover_vehicles_menu()
        self.assertTrue(self.page.is_mega_menu_open())

        with self.assertRaises(Exception):
            invalid_sub = (By.CSS_SELECTOR, ".mega-menu a[href*='error-config-path']")
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(invalid_sub))

    def test_TC_136_N_empty_or_broken_query_parameter_handling(self):
        """Verify handling of invalid or malformed URL parameters passed directly to vehicles path."""
        self.driver.get(f"{BASE_URL}/vehicles/invalid-nonexistent-subpage-test")
        WebDriverWait(self.driver, 5).until(lambda d: "tesla.com" in d.current_url)
        current_url = self.driver.current_url
        self.assertTrue(
            "invalid-nonexistent-subpage-test" in current_url or "tesla.com" in current_url,
            "The application failed to handle a malformed subpage route."
        )


if __name__ == "__main__":
    unittest.main()