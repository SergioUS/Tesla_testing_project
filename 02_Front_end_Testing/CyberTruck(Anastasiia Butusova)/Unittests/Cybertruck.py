#Anastasiia Butusova

import random
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def setUp(self):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=service)
    self.driver.maximize_window()

def delay():
    time.sleep(random.randint(1, 5))

class TeslaCybertruckChrome(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

# In TC 006 I need to check visibility and clickability of Tesla Cybertruck page.

    def test_case_006(self):
        driver = self.driver
        print("Test case 006:Cybertrack page is visible in the Header and the link is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        print("Test passed: Cybertrack page is working as expected")

# In TC 007 I need to check if Features and Accessories buttons work correctly.

    def test_case_007(self):
        driver = self.driver
        print("Test case 007:All sliders buttons of Features and Accessories work correctly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        driver.execute_script("window.scrollTo(0,1200)")
        time.sleep(5)
        driver.find_element(By.XPATH, "(//button[@type='button'])[37]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[38]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[39]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[40]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[41]").click()
        time.sleep(3)
        print("Test passed: Slider buttons are working as expected.")

# In TC 008 I need to check opening of CYBERTRUCK OFF-ROAD GUIDE page.

    def test_case_008(self):
        driver = self.driver
        print("Test case 008:CYBERTRUCK OFF-ROAD GUIDE opens properly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        driver.execute_script("window.scrollTo(0,3200)")
        time.sleep(5)
        window_before=driver.window_handles[0]
        driver.find_element(By.XPATH, "//span[contains(.,'View Cybertruck Off-Road Guide')]").click()
        time.sleep(7)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        if "cybertruck_offroad_guide" in driver.current_url:
            print("Test passed: CYBERTRUCK OFF-ROAD GUIDE was opened as expected")
        else:
            print("Test failed: CYBERTRUCK OFF-ROAD GUIDE was not opened")

#In TC 009 I need to check cklickability of ORDER NOW button.

    def test_case_009(self):
        driver = self.driver
        print("Test case 009:ORDER NOW button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[@href='cybertruck/design']").click()
        time.sleep(5)
        print("Test passed: ORDER NOW button is clickable as expected")

# In TC 010 I need to check clickability of DEMO DRIVE button.

    def test_case_010(self):
        driver = self.driver
        print("Test case 010:DEMO DRIVE button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        print("Test passed: DEMO DRIVE button is clickable as expected")

# In TC 006-6 I need to check if I can book Demo Drive of Cybertruck without entering First Name.

    def test_case_006_6(self):
        driver = self.driver
        print("Test case 006-6:User hasn't entered First Name in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        lastname_input = driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")

# In TC 007-7 I need to check if I can book Demo Drive of Cybertruck entering numbers in the First Namen field.

    def test_case_007_7(self):
        driver = self.driver
        print("Test case 007-7:User has entered numbers in the line 'First Name'' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("1112223334467")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")

# In TC 008-8 I need to check if I can book Demo Drive of Cybertruck entering gaps in the First Namen field.

    def test_case_008_8(self):
        driver = self.driver
        print("Test case 008-8:User has entered gaps in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("     ")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")

# In TC 009-9 I need to check if I can book Demo Drive of Cybertruck entering special symbols in the First Namen field.

    def test_case_009_9(self):
        driver = self.driver
        print("Test case 009-9:User has entered !@#$% in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")

# In TC 006-6 I need to check if I can book Demo Drive of Cybertruck without entering Email.

    def test_case_010_10(self):
        driver = self.driver
        print("Test case 010-10:User hasn't entered Email in the line 'Email' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")

    def tearDown(self):
        self.driver.quit()




class TeslaCybertruckFirefox(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()

    def test_case_006(self):
        driver = self.driver
        print("Test case 006:Cybertrack page is visible in the Header and the link is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        print("Test passed: Cybertrack page is visible in the Header and the link is clickable")
        driver.quit()


    def test_case_007(self):
        driver = self.driver
        print("Test case 007:All sliders buttons of Features and Accessories work correctly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        driver.execute_script("window.scrollTo(0,1200)")
        time.sleep(5)
        driver.find_element(By.XPATH, "(//button[@type='button'])[37]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[38]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[39]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[40]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[41]").click()
        time.sleep(3)
        print("Test passed: Slider buttons are working as expected.")
        driver.quit()

    def test_case_008(self):
        driver = self.driver
        print("Test case 008:CYBERTRUCK OFF-ROAD GUIDE opens properly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        driver.execute_script("window.scrollTo(0,3200)")
        time.sleep(5)
        window_before=driver.window_handles[0]
        driver.find_element(By.XPATH, "//span[contains(.,'View Cybertruck Off-Road Guide')]").click()
        time.sleep(7)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        if "cybertruck_offroad_guide" in driver.current_url:
            print("Test passed: CYBERTRUCK OFF-ROAD GUIDE was opened as expected")
        else:
            print("Test failed: CYBERTRUCK OFF-ROAD GUIDE was not opened")
        driver.quit()

    def test_case_009(self):
        driver = self.driver
        print("Test case 009:ORDER NOW button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[@href='cybertruck/design']").click()
        time.sleep(5)
        print("Test passed: ORDER NOW button is clickable as expected")
        driver.quit()

    def test_case_010(self):
        driver = self.driver
        print("Test case 010:DEMO DRIVE button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        print("Test passed: DEMO DRIVE button is clickable as expected")
        driver.quit()

    def test_case_006_6(self):
        driver = self.driver
        print("Test case 006-6:User hasn't entered First Name in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        lastname_input = driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")
        driver.quit()

    def test_case_007_7(self):
        driver = self.driver
        print("Test case 007-7:User has entered numbers in the line 'First Name'' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("1112223334467")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")
        driver.quit()

    def test_case_008_8(self):
        driver = self.driver
        print("Test case 008-8:User has entered gaps in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("     ")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")
        driver.quit()

    def test_case_009_9(self):
        driver = self.driver
        print("Test case 009-9:User has entered !@#$% in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")
        driver.quit()


    def test_case_010_10(self):
        driver = self.driver
        print("Test case 010-10:User hasn't entered Email in the line 'Email' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        cybertruck_img = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Cybertruck'])[1]"))
        )
        cybertruck_img.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
                print("Test Passed:Required input field")
        driver.quit()

    def tearDown(self):
        self.driver.quit()

class TeslaCybertruckEdge(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def test_case_006(self):
        driver = self.driver
        print("Test case 006:Cybertrack page is visible in the Header and the link is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        print("Test passed: Cybertrack page is working as expected")

    def test_case_007(self):
        driver = self.driver
        print("Test case 007:All sliders buttons of Features and Accessories work correctly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        driver.execute_script("window.scrollTo(0,1200)")
        time.sleep(5)
        driver.find_element(By.XPATH, "(//button[@type='button'])[37]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[38]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[39]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[40]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[41]").click()
        time.sleep(3)
        print("Test passed: Slider buttons are working as expected.")

    def test_case_008(self):
        driver = self.driver
        print("Test case 008:CYBERTRUCK OFF-ROAD GUIDE opens properly")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        driver.execute_script("window.scrollTo(0,3200)")
        time.sleep(5)
        window_before = driver.window_handles[0]
        driver.find_element(By.XPATH, "//span[contains(.,'View Cybertruck Off-Road Guide')]").click()
        time.sleep(7)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        if "cybertruck_offroad_guide" in driver.current_url:
            print("Test passed: CYBERTRUCK OFF-ROAD GUIDE was opened as expected")
        else:
            print("Test failed: CYBERTRUCK OFF-ROAD GUIDE was not opened")

    def test_case_009(self):
        driver = self.driver
        print("Test case 009:ORDER NOW button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='cybertruck/design']").click()
        time.sleep(5)
        print("Test passed: ORDER NOW button is clickable as expected")

    def test_case_010(self):
        driver = self.driver
        print("Test case 010:DEMO DRIVE button is clickable")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        print("Test passed: DEMO DRIVE button is clickable as expected")

    def test_case_006_6(self):
        driver = self.driver
        print("Test case 006-6:User hasn't entered First Name in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
            print("Test Passed:Required input field")

    def test_case_007_7(self):
        driver = self.driver
        print("Test case 007-7:User has entered numbers in the line 'First Name'' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("1112223334467")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
            print("Test Passed:Required input field")

    def test_case_008_8(self):
        driver = self.driver
        print("Test case 008-8:User has entered gaps in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("     ")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
            print("Test Passed:Required input field")

    def test_case_009_9(self):
        driver = self.driver
        print("Test case 009-9:User has entered !@#$% in the line 'First Name' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys("bu2soffa@gmail.com")
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
            print("Test Passed:Required input field")

    def test_case_010_10(self):
        driver = self.driver
        print("Test case 010-10:User hasn't entered Email in the line 'Email' of Demo Drive Cybertruck")
        driver.get("https://www.tesla.com/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      "//span[@class='tds-site-nav-item-text'][contains(.,'Vehicles')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element = driver.find_element(By.XPATH, "(//img[@alt='Cybertruck'])[1]")
        element.click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/drive?selectedModel=Cybertruck']").click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(5)
        firstname_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname_input.send_keys("!@#$%")
        lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname_input.send_keys("Jackson")
        phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        phone_input.send_keys("424-677-00-00")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        try:
            if driver.find_element(By.XPATH, "//h1[@class='tds--no_padding'][contains(.,'Thank You')]"):
                print("Test Failed:Demo Drive was booked")
        except NoSuchElementException:
            print("Test Passed:Required input field")

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()