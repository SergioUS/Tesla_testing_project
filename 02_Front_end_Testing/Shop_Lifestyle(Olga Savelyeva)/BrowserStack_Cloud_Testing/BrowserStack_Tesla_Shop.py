#https://automate.browserstack.com/builds/bf2aa95dec804aec5201ca180899ad0381e34f09/sessions/8e31878728f370b60bc22871b2e8c1f78408d472?auth_token=32576a9a22162db7854503f16d424251528dbc80696b3a4073bb8e21ba557dd3
#OS: Windows, Version: 10, Browser: Chrome 131.0

#https://automate.browserstack.com/builds/bf2aa95dec804aec5201ca180899ad0381e34f09/sessions/20185a608fd3e12fc30da0c7b23bb776e46b59b6?auth_token=5d190a54d4d99735f413635b58cd02352f36f865a14681bd1f929db9f963e1ab
#OS: Windows, Version: 10, Browser: Edge 131.0

#https://automate.browserstack.com/builds/bf2aa95dec804aec5201ca180899ad0381e34f09/sessions/19445e26e2b8b3a215ffa35a92c88197b997445b?auth_token=29d3837f673032854f4796da4dfd462b353cd47b60609de32697b201143eab07
#OS: Windows, Version: 10, Browser: Firefox 133.0

#https://automate.browserstack.com/builds/5556cb6458f76ba1d57014a50370accf5fdbd80e/sessions/c60dc58bffbfbfe01de3f79d8c92f6c15fc3ada8?auth_token=72a72a47634213bd6a4ca54428af180f9f5ea9bc745c12d95bbd8f4b8315ef3b
#OS: OX Sonoma, Browser: edge 132.0 beta

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def delay():
    time.sleep(random.randint(1, 5))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.tesla.com/')
driver.maximize_window()
time.sleep(6)

# Verify page's title
try:
    assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
       print("Title is different. Current Title is:", driver.title)
delay()
# Verify page's elements/buttons
driver.find_element(By.XPATH, "//header/h1[1]/a[1]/*[1]")
driver.find_element(By.XPATH, "//span[contains(.,'Charging')]")
driver.find_element(By.XPATH, "(//span[contains(.,'Energy')])[1]")
driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()
time.sleep(1)

# Verify page's title
try:
    assert driver.title == "The Official Tesla Shop | Tesla"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)
delay()

# Verify button "Lifestyle" is visible and clickable
driver.find_element(By.XPATH, "(//a[@href='/category/lifestyle'])[1]").click()
print("Lifestyle button is visible and clickable")
time.sleep(1)

driver.back()
driver.forward()

# Verify page's title
try:
    assert driver.title == "Tesla | Lifestyle"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)
delay()

# Verify page's elements/buttons
driver.find_element(By.ID, "lifestyle.best-sellers")
driver.find_element(By.ID, "page--category")
driver.find_element(By.ID, "lifestyle.bags")
driver.find_element(By.ID, "left-menu__logo")

# go down find product
driver.execute_script("window.scrollTo(0,6000)")
time.sleep(10)

driver.find_element(By.XPATH, "(//img[@alt='Wireless Portable Charger'])[1]").is_displayed()
print("Picture of Charger is displayed")
driver.find_element(By.XPATH, "(//a[contains(.,'Wireless Portable Charger')])[1]").is_displayed()
print("Text of Charger is displayed")


# quit from browser
driver.quit()
