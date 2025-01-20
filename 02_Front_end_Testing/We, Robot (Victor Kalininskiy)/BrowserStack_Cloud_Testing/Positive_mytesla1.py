
# Positive test TC-090

import time
import unittest
import random
from logging import exception

from dash.testing.wait import until
from openpyxl.styles.builtins import title
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common import WebDriverException as WDE, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# coding=utf8

from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

import random
from selenium import webdriver
from selenium.webdriver.common.by import By


# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)


# randomly sleep between 1 and 2 seconds
def delay():
    time.sleep(random.randint(1, 2))

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.tesla.com/en_CA/")
driver.maximize_window()

delay()

# click on Esc button to close overlay
pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
pressesc.send_keys(Keys.ESCAPE)
time.sleep(1)

# Finding and clicking on 'We, Robot' link
try:
    # clicking on 'We, Robot' link
    werobot_link = WebDriverWait(driver, 2).until(EC.presence_of_element_located((
        By.ID, "dx-nav-item--we-robot")))
    werobot_link.click()
    print("The link 'We, Robot' was clicked")

    # checking for correct title in 'We, Robot' page
    assert "We, Robot | Tesla" in driver.title
    print("'We, Robot' page is open and the title is correct")
except NoSuchElementException:
     print("No presence of 'We, Robot' link' on main page")

driver.close()
print("Test Case #090 passed \n")
