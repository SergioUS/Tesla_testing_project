# https://automate.browserstack.com/builds/6dcb5e9ef2f51b4c18cfdd04377412f7ccc83097/sessions/db33b19afd2dbf0b7b7ba99e173dec4edfce7b22?auth_token=a15353d9d2ce1ac4aa9adacc944dd8716ca842bb25f016e82ce636d57591dda3
# https://automate.browserstack.com/builds/6dcb5e9ef2f51b4c18cfdd04377412f7ccc83097/sessions/ed4e1caccf49e654bbadaa406424c32f307efb8b?auth_token=7ea81535c199b80edbdae3c01819fdfbad9fee3ad84dcbba2797a1aba8bcce0a

import time
import random

from selenium.common import WebDriverException as WDE
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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# opening website 1. Enter http://tesla.com
driver.get("https://www.tesla.com/")
driver.maximize_window()

# 2. Hover the mouse over the button "Shop" in the header
delay()
element_to_hover = driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']")
# Create an ActionChains object
action = ActionChains(driver)
# Perform the hover action
action.move_to_element(element_to_hover).perform()

#3. Click the "Apparel" button
driver.find_element(By.XPATH, "//img[@alt='Apparel']").click()

# 4. Verify that correct page is open ("Apparel")
try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'men.best-sellers')))
    print("You are on the page 'Apparel'")
except WDE:
    print("The page is not correct!!!")

driver.quit()