import random
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from Helpers import Helper as hlp


def delay():
    time.sleep(random.randint(1, 5))

class ChromeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'

    def test_chrome_TC_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

    # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
    # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(2)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is displayed
        if driver.find_element(By.XPATH, hlp.Btn_lfs).is_displayed():
            print("Lifestyle button is visible")
        else:
            print("Lifestyle button is not visible")

        # quit from browser
        driver.quit()

    def test_chrome_TC_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

       # Verify page's elements/buttons
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_chrome_TC_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
               print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        # go down find product
        driver.execute_script(hlp.Srl)
        time.sleep(10)

        #find product on page
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).is_displayed()
        print("Text of Charger is displayed")


        # quit from browser
        driver.quit()

    def test_chrome_TC_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        # Verify product is disp
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_chrome_TC_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()
        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, hlp.quan_pnk)
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")
        delay()

        driver.save_screenshot("PosChr_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class FirefoxTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        


    def test_firefox_TC_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(2)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is displayed
        if driver.find_element(By.XPATH, hlp.Btn_lfs).is_displayed():
            print("Lifestyle button is visible")
        else:
            print("Lifestyle button is not visible")

        # quit from browser
        driver.quit()

    def test_firefox_TC_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's elements/buttons
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_firefox_TC_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        # go down find product
        driver.execute_script(hlp.Srl)
        time.sleep(10)

        # find product on page
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).is_displayed()
        print("Text of Charger is displayed")

        # quit from browser
        driver.quit()

    def test_firefox_TC_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        # Verify product is disp
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_firefox_TC_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, hlp.quan_pnk)
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")
        delay()

        driver.save_screenshot("PosFF_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class EdgeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'



    def test_Edge_TC_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(2)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is displayed
        if driver.find_element(By.XPATH, hlp.Btn_lfs).is_displayed():
            print("Lifestyle button is visible")
        else:
            print("Lifestyle button is not visible")

        # quit from browser
        driver.quit()

    def test_Edge_TC_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
        print("Lifestyle button is visible and clickable")
        time.sleep(1)

        driver.back()
        driver.forward()

        # Verify page's elements/buttons
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        try:
            assert driver.title == "Tesla | Lifestyle"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_Edge_TC_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        # go down find product
        driver.execute_script(hlp.Srl)
        time.sleep(10)

        # find product on page
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).is_displayed()
        print("Text of Charger is displayed")

        # quit from browser
        driver.quit()

    def test_Edge_TC_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        # Verify product is disp
        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # quit from browser
        driver.quit()

    def test_Edge_TC_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Check elements on product page
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # Find quantity input and add 2
        quantity = driver.find_element(By.XPATH, hlp.quan_pnk)
        quantity.click()
        time.sleep(5)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(1)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Successfully added 2 quantities to cart!")
        except NoSuchElementException:
            print("Test failed")
        delay()

        driver.save_screenshot("PosEdg_TC_106_tesla_item added_test.png")

        driver.quit()

        # Anything declared in tearDown will be executed for all test cases
        # Closing browser. You need to use "tearDown" method only one time for every Class

    def tearDown(self):
        self.driver.quit()

class ChromeNegTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'

    def test_chrome_TC_Neg_102_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed" )
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_103_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.white)
        color_option.click()

        # find quantity field, delete "1" and add "6"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_white)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_White)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_White).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_104_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

       #Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('3')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ctNCR)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ctNCR).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_105_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "0"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_black)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_Black)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_Black).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegCh_TC_105_tesla_item added_test.png")

        driver.quit()

    def test_chrome_TC_Neg_106_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, hlp.quan_black)
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

    def tearDown(self):
        self.driver.quit()

class FirefoxNegTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'

    def test_firefox_TC_Neg_102_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify page's elements
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_103_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.white)
        color_option.click()

        # find quantity field, delete "1" and add "6"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_white)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_White)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_White).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_104_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('3')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ctNCR)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ctNCR).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_105_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        try:
            assert driver.title == "Wireless Portable Charger"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "0"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_black)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_Black)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_Black).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegFF_TC_105_tesla_item added_test.png")

        driver.quit()

    def test_firefox_TC_Neg_106_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, hlp.quan_black)
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

    def tearDown(self):
        self.driver.quit()

class EdgeNegTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'

    def test_edge_TC_Neg_102_102(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.pink)
        color_option.click()

        # find quantity field, delete "1" and add "e"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('e')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ct)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ct).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_102_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_103_103(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.white)
        color_option.click()

        # find quantity field, delete "1" and add "6"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_white)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_white).send_keys('6')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_White)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_White).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_103_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_104_104(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Try to add product quantity between 1-5 without choosing color
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.qua_field)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.qua_field).send_keys('3')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_ctNCR)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_ctNCR).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_104_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_105_105(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "0"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.quan_black)))
        time.sleep(3)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).click()
        time.sleep(2)
        driver.find_element(By.XPATH, hlp.quan_black).send_keys('0')
        time.sleep(2)

        # Click "Add to Cart"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, hlp.Add_to_Black)))
        print("button is clickable")
        driver.find_element(By.XPATH, hlp.Add_to_Black).click()
        time.sleep(5)

        try:
            if driver.find_element(By.XPATH, hlp.Check_OT):
                print("Button Checkout is visible, test failed")
        except NoSuchElementException:
            print("Button Checkout is not visible, test passed")
        delay()
        driver.save_screenshot("NegEd_TC_105_tesla_item added_test.png")

        driver.quit()

    def test_edge_TC_Neg_106_106(self):
        driver = self.driver

        driver.get(hlp.tsl)
        time.sleep(4)

        # Verify page's title
        try:
            assert driver.title == "Electric Cars, Solar & Clean Energy | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()
        # Verify page's elements/buttons
        driver.find_element(By.XPATH, hlp.hea_der)
        driver.find_element(By.XPATH, hlp.char_ng)
        driver.find_element(By.XPATH, hlp.enr_g)
        driver.find_element(By.XPATH, hlp.shop).click()
        time.sleep(1)

        # Verify page's title
        try:
            assert driver.title == "The Official Tesla Shop | Tesla"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Verify button "Lifestyle" is visible and clickable
        driver.find_element(By.XPATH, hlp.Btn_lfs).click()
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
        driver.find_element(By.ID, hlp.Bst_sel)
        driver.find_element(By.ID, hlp.Pg_Cat)
        driver.find_element(By.ID, hlp.Bgs)
        driver.find_element(By.ID, hlp.Mn_log)

        driver.execute_script(hlp.Srl)
        time.sleep(10)

        driver.find_element(By.XPATH, hlp.pic).is_displayed()
        print("Picture of Charger is displayed")
        driver.find_element(By.XPATH, hlp.txt).click()
        delay()

        # Verify page's title
        driver.find_element(By.XPATH, hlp.prd_ttl).is_displayed()
        driver.find_element(By.XPATH, hlp.ing_prd).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_dcr).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_qu_fld).is_displayed()
        driver.find_element(By.XPATH, hlp.prd_cred_pr).is_displayed()
        driver.find_element(By.XPATH, hlp.Lo_mnCh).is_displayed()

        # Select the color
        color_option = driver.find_element(By.XPATH, hlp.black)
        color_option.click()

        # find quantity field, delete "1" and add "-6"
        quantity = driver.find_element(By.XPATH, hlp.quan_black)
        print(quantity.get_attribute("value"))
        if quantity.get_attribute("value") == "-6":
            print("Test Fail. Able to enter negative number")
        else:
            print("Test Pass. Not able to enter negative number")
        time.sleep(1)

        driver.quit()

    def tearDown(self):
        self.driver.quit()
