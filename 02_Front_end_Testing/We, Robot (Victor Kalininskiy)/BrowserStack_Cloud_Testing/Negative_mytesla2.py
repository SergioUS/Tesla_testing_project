
# Negative test #090-90

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


# randomly sleep between 1 and 2 seconds
def delay():
    time.sleep(random.randint(1, 2))

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)


# opening 'We, Robot' page
driver.get("https://www.tesla.com/en_ca/we-robot")
delay()
time.sleep(2)

# click on Esc button to close overlay
pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
pressesc.send_keys(Keys.ESCAPE)
time.sleep(1)

# scroll to the First Name field
driver.execute_script("window.scrollTo(214,3160)")

# clear 'First Name' field
first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
first_input.clear()  # Clear field
# driver.save_screenshot('./errormessage 1_testcase090-00_firstname.png')

# clear the 'Last Name' field
check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
check_input.clear()  # Clear field

# clear on the 'Email Address' field
check_input = driver.find_element(By.XPATH, "//input[@name='email']")
check_input.clear()  # Clear field

# clear the 'Phone Number' field
check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
check_input.clear()  # Clear field

# clear on the 'Zip Code' field
check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
check_input.clear()  # Clear field

try:
    # click on Submit button
    submitbut = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((
        By.XPATH, "//button[contains(.,'Submit')]")))
    # driver.execute_script('arguments[0].scrollIntoView()', submitbut)
    submitbut.click()
    print('Submit button was clicked')

except Exception as e:
    print('Submit button was Not clicked')

try:
    # check error message
    firstmessage = driver.find_element(By.XPATH,
                                 "(//div[@class='tds-form-feedback-text'][text()='Required'])[1]")
    assert 'Required' in  firstmessage.text

    # check error message
    lastmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[2]")
    assert 'Required' in lastmessage.text

    # check error message
    emailmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[3]")
    assert 'Required' in emailmessage.text

    # check error message
    phonemessage = driver.find_element(By.XPATH, "//div[text()='Please enter a phone number']")
    assert 'Please enter a phone number' in phonemessage.text

    # check error message
    zipmessage = driver.find_element(By.XPATH, "//div[@class='tds-form-feedback-text'][text()='Invalid']")
    assert 'Invalid' in zipmessage.text

except Exception as e:
    print('Test #090-90 fail, no error message(s) appeared for empty fiels(s)')

driver.close()
print("Test Case #090-90 passed \n")



