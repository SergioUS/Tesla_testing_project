#https://automate.browserstack.com/builds/b457b16849c5a46b0973dfd0f5aeae3d9117a1e3/sessions/0240f2a325d9b425e01dd7800724ba75c1bbf202?auth_token=68403d0faa886349492a261480ca8b1f5b44b35f8b619ed173ae01a834efcea8

# BR080: Verify that languages button is clickable and client can change languages (English, Spanish, French).
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

def delay():
    time.sleep(random.randint(1, 4))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Step 1: Open Tesla Solar Panels page
print("Step 1: Open Tesla Solar Panels page.")
driver.get("https://www.tesla.com/solarpanels")
delay()

# Step 2: Find and click the 'Languages' button
print("Step 2: Find and click the 'Languages' button.")
try:
    driver.find_element(By.XPATH, "//button[@id='dx-nav-item--locale-selector']").click()
    print("'Languages' button clicked successfully.")
except:
    print("Could not find or click the 'Languages' button.")
    #return

delay()

# Step 3: Select Spanish language
print("Step 3: Select Spanish language.")
try:
    driver.find_element(By.XPATH, "//a[contains(text(), 'Español')]").click()
    print("Switched to Spanish language successfully.")
except:
    print("Could not switch to Spanish language.")
    #return
driver.quit()
