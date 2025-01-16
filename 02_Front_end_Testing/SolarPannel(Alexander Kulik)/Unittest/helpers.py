import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def delay(min_seconds=1, max_seconds=4):
    time.sleep(random.randint(min_seconds, max_seconds))

def log_message(message):
    from datetime import datetime
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: {message}")

def find_and_click(driver, by, value):
    try:
        element = driver.find_element(by, value)
        element.click()
        log_message(f"Clicked element: {value}")
        return True
    except NoSuchElementException:
        log_message(f"Element not found: {value}")
        return False

def wait_for_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        log_message(f"Element found: {value}")
        return element
    except NoSuchElementException:
        log_message(f"Timeout waiting for element: {value}")
        return None

    from selenium.webdriver.common.by import By

    class Locators:
        # Tesla Solar Panel Page Locators
        ENERGY_BUTTON = (By.XPATH, "//h2[contains(text(),'Energy')]")
        SOLAR_PANEL_OPTION = (By.XPATH, "//a[text()='Solar Panels']")
        ORDER_NOW_BUTTON = (By.XPATH, "(//span[contains(.,'Order Now')])[1]")
        CONSULTATION_BUTTON = (By.XPATH, "(//a[contains(.,'Schedule a Consultation')])[2]")
        LANGUAGE_BUTTON = (By.XPATH, "//button[@id='dx-nav-item--locale-selector']")
        SPANISH_OPTION = (By.XPATH, "//a[contains(text(), 'Español')]")
        CHAT_BUTTON = (By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']")
        AVERAGE_BILL_INPUT = (By.XPATH, "//input[@name='electric-bill']")
        ERROR_MESSAGE = (By.XPATH, "//h1[contains(text(),'404')]")
        NEXT_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")
        INVALID_BILL_ERROR = (By.XPATH, "//div[contains(text(),'Invalid')]")