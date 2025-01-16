
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

import helpers

# randomly sleep between 1 and 4 seconds
def delay():
    time.sleep(random.randint(1, 2))

class NoSuchElementException:
    pass


class ChromePositiveTests(unittest.TestCase):

    # The class setUp. I will have 3 (chrome,firefox,edge)
    def setUp(self):

        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('--lang=en-US')
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(service=service, options=options)
        options.add_argument('--user-data-dir=/path/to/fresh/profile')
        self.driver.maximize_window()


    def test_chrome_090(self):
        driver = self.driver
        # opening Tesla website
        driver.get(helpers.main)
        delay()

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

        self.driver.close()
        print("Test Case #090 passed \n")


    def test_chrome_091(self):
        driver = self.driver
        # opening 'We, Robot' page
        driver.get(helpers.mytestpage1)
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # checking for correct title in 'We, Robot' page
        assert "We, Robot | Tesla" in driver.title
        print("Title of 'We, Robot' page is correct")

        # Finding and clicking on 'Logo' link
        try:
            # clicking on 'Tesla' logo link
            werobot_link = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((
                By.XPATH, " //a[@aria-label='Tesla Logo']")))
            werobot_link.click()
            print("Tesla logo was clicked")
        except NoSuchElementException:
            print("No presence of 'Tesla' Logo on 'We, Robot' page")

        delay()

        # checking for 'We, Robot' page is open
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("The main page is open and title is correct")
        except NoSuchElementException:
             print("The main page is Not open")

        self.driver.close()
        print("Test Case #091 passed \n")


    def test_chrome_092(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # check WE ROBOT image
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@class='tds-icon tds-icon-logo-we-robot-alt']")))
            print("WE, ROBOT image was found")
        except NoSuchElementException:
            print("WE, ROBOT image was not found")

        futureautonomus = driver.find_element(By.XPATH, "// h2[contains(., 'The Future Is Autonomous')]")
        helpers.assert_subtitles('The Future Is Autonomous', futureautonomus)
        # check if iframe with video exists
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "twitter-widget-0")))
            print("iframe with video for ‘The Future Is Autonomous’ exits")
        except NoSuchElementException:
            print("iframe with video for ‘The Future Is Autonomous’ not found")

        autonomy = driver.find_element(By.XPATH, " //h2[contains(.,'Autonomy for All')]")
        helpers.assert_subtitles('Autonomy for All', autonomy)

        robotaxi = driver.find_element(By.XPATH, "//span[contains(., 'Robotaxi')]")
        helpers.assert_subtitles('Robotaxi', robotaxi)
        #check Robotaxi image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt = 'Robotaxi']")))
            print("Image for ‘Robotaxi’ was found")
        except NoSuchElementException:
            print("Image for ‘Robotaxi’ was Not found")

        robovan = driver.find_element(By.XPATH, "//span[contains(.,'Robovan')]")
        helpers.assert_subtitles('Robovan', robovan)
        # check Robovan image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Robovan']")))
            print("Image for ‘Robovan’ was found")
        except NoSuchElementException:
            print("Image for ‘Robovan’ was Not found")

        teslabot = driver.find_element(By.XPATH, "//span[contains(.,'Tesla Bot')]")
        helpers.assert_subtitles('Tesla Bot', teslabot)
        # check Tesla Bot image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Optimus']")))
            print("Image for ‘Tesla Bot’ was found")
        except NoSuchElementException:
            print("Image for ‘Tesla Bot’ was Not found")

        autonomy2 = driver.find_element(By.XPATH, "(//span[contains(.,'Discover Autonomy')])[2]")
        helpers.assert_subtitles('Discover Autonomy', autonomy2)
        # check Discover Autonomy video
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "tesla-video-4261")))
            print("Video for 'Discover Autonomy' was found")
        except NoSuchElementException:
            print("Video for 'Discover Autonomy' was Not found")
        # check Discover Autonomy form
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "tesla-form-standalone-1546")))
            print("Form for 'Discover Autonomy' was found")
        except NoSuchElementException:
            print("Form for 'Discover Autonomy' was Not found")

        futureautonomus2 = driver.find_element(By.XPATH, "//h1[contains(.,'The Future is Autonomous')] ")
        helpers.assert_subtitles('The Future is Autonomous', futureautonomus2)
        # check subtitle
        futureautonomussub = driver.find_element(By.XPATH,
        "//p[contains(.,'Experience Full Self-Driving (Supervised) in any Tesla vehicle with a demo drive.')]")
        helpers.assert_subtitles('Experience Full Self-Driving (Supervised) in any Tesla vehicle with a demo drive.',
                                 futureautonomussub)
        # check image ‘The Future Is Autonomous’ at the bottom page
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dx-end-content']")))
            print("Image for ‘The Future Is Autonomous’ was found")
        except NoSuchElementException:
            print("Image for ‘The Future Is Autonomous’ was Not found")

        # check button 'Experience Tesla' at the bottom page
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Experience Tesla')]")))
            print("Button 'Experience Tesla' was found")
        except NoSuchElementException:
            print("IButton 'Experience Tesla' was Not found")

        self.driver.close()
        print("Test Case #092 passed \n")


    def test_chrome_093(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(1)

        # Store the ID of the original window
        original_window = driver.current_window_handle
        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1

          # variant 1 :
        # Finding and clicking on the link 'Watch on X/Continue watching on X' inside the iframe

        # scroll to the link  'Watch on X/Continue watching on X' was visible
        driver.execute_script("window.scrollTo(0,600)")

        # wait iframe and switch to
        iframewathch = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,
                                                                                      "twitter-widget-0")))
        driver.switch_to.frame(iframewathch)
        print("Swith to iFrame done")
        delay()
        
        try:
            #  click on link open new Tab
            driver.find_element(By.XPATH, "(//a[starts-with(@href, 'https://twitter.com/Tesla/status/')])[2]").click()
            print("The link 'Continue watching on X/Watch on X' was clicked")
        except NoSuchElementException:
            print("The link 'Continue watching on X/Watch on X' was Not clicked")

         # Wait for the new tab
        WebDriverWait(driver, 1).until(EC.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                print("Switch to new tab done")
                break

        try:
            # assert URL open
            WebDriverWait(driver, 4).until(EC.url_contains('https://x.com/Tesla/'))
            # assert the title of the 'X' page is being open
            WebDriverWait(driver, 4).until(EC.title_is(
                'Tesla on X: "The future will be streamed live 10/10, 7pm PT https://t.co/YJEjZIYoTA" / X'))
            # WebDriverWait(driver, 4).until(EC.title_contains('Tesla on X:'))
            print("The new Tesla page in 'X' is open and the title is correct")
            print(driver.title)
        except NoSuchElementException:
            print("The new Tesla page in 'X' is not open")
        
        #Switch back to the old tab or window
        driver.switch_to.window(original_window)
        
        '''
        # variant 2 : open X page with direct URL  instead of  clicking link 'Continue watching on X'

        # Opens a new tab and switches to new tab
        driver.switch_to.new_window('tab')

        # Load a new 'X' page
        driver.get(
            "https://twitter.com/Tesla/status/1843922599765590148?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1843922599765590148%7Ctwgr%5Eedc586053e267ec694fe0d2d476dec65c7865714%7Ctwcon%5Es1_&amp;ref_url=https%3A%2F%2Fwww.tesla.com%2Fen_ca%2Fwe-robot")

        try:
            # Wait for the new tab to finish loading content
            WebDriverWait(driver, 3).until(EC.title_contains('Tesla on X: "The future will be streamed live '))
            print("The new Tesla page in 'X' is open and the title is: \n" + driver.title)
        except NoSuchElementException:
            print("The new Tesla page in 'X' is not open")
        '''

        self.driver.close()
        print("Test Case #093 passed \n")


    def test_chrome_094(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        driver.execute_script("window.scrollTo(0,2400)")
        time.sleep(1)

        # click on Robotaxi text
        driver.find_element(By.XPATH, "//span[contains(., 'Robotaxi')]").click()
        # check Robotaxi image open
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt = 'Robotaxi']")))
            print("Image for ‘Robotaxi’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Robotaxi’ was Not  displayed")

        # click on Robovan text
        driver.find_element(By.XPATH, "//span[contains(.,'Robovan')]").click()
        # check Robovan image open
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Robovan']")))
            print("Image for ‘Robovan’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Robovan’ was Not displayed")

        # click on Tesla Bot text
        driver.find_element(By.XPATH, "//span[contains(.,'Tesla Bot')]").click()
        # check Tesla Bot image open
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Optimus']")))
            print("Image for ‘Tesla Bot’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Tesla Bot’ was Not displayed")

        self.driver.close()
        print("Test Case #094 passed \n")


    def test_chrome_095(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # scroll to the First Name field with offset
        driver.execute_script("window.scrollTo(214,3120)")
        #time.sleep(3)

        # check 'First Name' title
        firstname = driver.find_element(By.XPATH,  "//label[contains(.,'First Name')]")
        helpers.assert_subtitles('First Name', firstname)
        # print(first_name.location)

        # check 'Last Name' title
        lastname = driver.find_element(By.XPATH, "//label[contains(.,'Last Name')]")
        helpers.assert_subtitles('Last Name', lastname)

        # check 'Email Address' title
        emailaddress = driver.find_element(By.XPATH, "//label[contains(.,'Email Address')]")
        helpers.assert_subtitles('Email Address', emailaddress)

        # check 'Phone Number' title
        phonenum = driver.find_element(By.XPATH, "//label[contains(.,'Phone Number')]")
        helpers.assert_subtitles('Phone Number', phonenum)

        # check 'Zip Code' title
        zipcode = driver.find_element(By.XPATH, "//label[contains(.,'Zip Code')]")
        helpers.assert_subtitles('Zip Code', zipcode)

        # click   on the 'First Name' field and Enter, for all fields be clicked on one time
        # ...
        # check_input.send_keys(Keys.ENTER)
        #  all fields clicked screenshot
        # driver.save_screenshot('./image.png')

        # click on the 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        driver.save_screenshot('./errormessage_testcase095_firstname.png')
        first_input.click()
        # click on title , for error message be appeared
        firstname.click()
        # check error message
        firstmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[1]")
        helpers.assert_subtitles('Required', firstmessage)

        # click on the 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        lastname.click()
        # check error message
        lastmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[2]")
        helpers.assert_subtitles('Required', lastmessage)

        # click on the 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        emailaddress.click()
        # check error message
        emailmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[3]")
        helpers.assert_subtitles('Required', emailmessage)

        # click on the 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        phonenum.click()
        # check error message
        phonemessage = driver.find_element(By.XPATH, "//div[text()='Please enter a phone number']")
        helpers.assert_subtitles('Please enter a phone number', phonemessage)

        # click on the 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        zipcode.click()
        # check error message
        zipmessage = driver.find_element(By.XPATH, "//div[@class='tds-form-feedback-text'][text()='Invalid']")
        helpers.assert_subtitles('Invalid', zipmessage)

        self.driver.close()
        print("Test Case #095 passed \n")


    def test_chrome_096(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

        # scroll to the First Name field
        driver.execute_script("window.scrollTo(214,3160)")

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('Viktor')  # Enter text
        driver.save_screenshot('./errormessage_testcase096_firstname.png')

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('yoisaneimmoucro-5378@yopmail.com')  # Enter text

        # enter value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(415) 555-1234') # Enter text

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('94111') # Enter text

        try:
            # click on Submit button
            submitbut = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((
                By.XPATH, "//button[contains(.,'Submit')]")))
            #driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            submitbut.click()
            print('Submit button was clicked')

            WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(.,'Thank you')]")))
            print("Test Case #096 passed \n")

        except Exception as e:
            # check error message
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
                 (By.XPATH, "//div[@class='tds-form-feedback-text'][text()='Invalid']")))
            print('Test #096 fail, error message appeared for valid ZIP code')

            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase096_01.png')
            return None

        self.driver.close()

    def tearDown(self):
        self.driver.quit()
        

    print("-------------------------------------NEGATIVE TEST CASES CHROME---------------------------------- \n")

    class ChromeNegativeTests(unittest.TestCase):

        # The class setUp. I will have 3 (chrome,firefox,edge)
        def setUp(self):
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            options.add_argument('--lang=en-US')
            options.page_load_strategy = 'eager'
            self.driver = webdriver.Chrome(service=service, options=options)
            options.add_argument('--user-data-dir=/path/to/fresh/profile')
            self.driver.maximize_window()

    def test_chrome_090_90(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # scroll to the First Name field
        driver.execute_script("window.scrollTo(214,3160)")

        # clear 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        driver.save_screenshot('./errormessage 1_testcase090-00_firstname.png')

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
            #driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            submitbut.click()
            print('Submit button was clicked')

        except Exception as e:
            print('Submit button was Not clicked')

        try:
            # check error message
            firstmessage = driver.find_element(By.XPATH,
                                               "(//div[@class='tds-form-feedback-text'][text()='Required'])[1]")
            helpers.assert_subtitles('Required', firstmessage)

            # check error message
            lastmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[2]")
            helpers.assert_subtitles('Required', lastmessage)

            # check error message
            emailmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[3]")
            helpers.assert_subtitles('Required', emailmessage)

            # check error message
            phonemessage = driver.find_element(By.XPATH, "//div[text()='Please enter a phone number']")
            helpers.assert_subtitles('Please enter a phone number', phonemessage)

            # check error message
            zipmessage = driver.find_element(By.XPATH, "//div[@class='tds-form-feedback-text'][text()='Invalid']")
            helpers.assert_subtitles('Invalid', zipmessage)

        except Exception as e:
            print('Test #096 fail, no error message(s) appeared for empty fiels(s)')
            # error message screenshot
            #driver.save_screenshot('./errormessage 2_testcase090-90.png')
            return None

        self.driver.close()
        print("Test Case #090-090 passed \n")


    def test_chrome_091_91(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        pressesc = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        pressesc.send_keys(Keys.ESCAPE)

        # scroll to the Last Name field
        driver.execute_script("window.scrollTo(214,3200)")
        time.sleep(1)
        #driver.save_screenshot('./errormessage_testcase091_91 -01.png')

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('yoisaneimmoucro-5378@yopmail.com')  # Enter text

        # enter value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(415) 555-1234') # Enter text

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('94111') # Enter text

        try:
            # click on Submit button
            submitbut = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((
                By.XPATH, "//button[contains(.,'Submit')]")))
            #driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            submitbut.click()
            print('Submit button was clicked')

            WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(.,'Thank you')]")))
            print("Test Case #091-091 passed \n")

        except Exception as e:
            print('Test #091-091 fail')
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase091_91 -02.png')
            return None

        self.driver.close()


    def test_chrome_092_92(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/en_ca/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

        # scroll to the First Name field
        driver.execute_script("window.scrollTo(214,4700)")
        time.sleep(2)
        #driver.save_screenshot('./errormessage_testcase092_92 -01.png')

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('Viktor')  # Enter text

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('yoisaneimmoucro-5378@yopmail.com')  # Enter text

        # enter value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(415) 555-1234')  # Enter text

        # clear 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        print(check_input.location)
        check_input.clear()  # Clear field

        try:
            # click on Submit button
            submitbut = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((
                By.XPATH, "//button[contains(.,'Submit')]")))
            # driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            submitbut.click()
            print('Submit button was clicked')

            # check error message
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='zip']")))
            print("Test Case #096 passed \n")
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase092_92 -02.png')
        except Exception as e:
            print('Test #092_92 fail, error message Not appeared ZIP code field')

            return None

        self.driver.close()


    def test_chrome_093_93(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/en_ca/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

        # scroll to the form
        driver.execute_script("window.scrollTo(214,4950)")
        time.sleep(2)
        #driver.save_screenshot('./errormessage_testcase093_93 -01.png')

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('1/2')  # Enter text

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('yoisaneimmoucro-5378@yopmail.com')  # Enter text

        # enter value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(416) 368-2511')  # Enter text

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('M5E 1E5')

        try:
            # click on Submit button
            submitbut = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((
                    By.XPATH, "//button[contains(.,'Submit')]")))
            # driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            print(check_input.location)
            submitbut.click()
            print('Submit button was clicked')

            # check error message
            firstmessage = driver.find_element(By.XPATH,
                                        "(//div[@class='tds-form-feedback-text'][text()='Required'])[1]")
            helpers.assert_subtitles('Required', firstmessage)
            print("Test Case #093_93 passed \n")
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase093_93 -02.png')
        except Exception as e:
            # check message data was sent
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(
                    (By.XPATH, "//h1[contains(.,'Thank you')]")))
            print('Test #093-93 fail, error message not displayed and the form was submitted')
            return None

        self.driver.close()


    def test_chrome_094_94(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/en_ca/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

        # scroll to the form
        driver.execute_script("window.scrollTo(214,4800)")
        time.sleep(2)
        #driver.save_screenshot('./errormessage_testcase094_94 -01.png')

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('Viktor')  # Enter text

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys(' ')  # Enter one blank space

        # enter value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(416) 368-2511')  # Enter text

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('M5E 1E5')

        try:
            # check error message
            emailmessage = driver.find_element(By.XPATH,
                                    "(//div[contains(.,'Invalid')])[12]")
            helpers.assert_subtitles('Invalid', emailmessage)
            print("Test Case #093_93 passed \n")
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase094_94 -02.png')
        except Exception as e:
            print('Test #093-93 fail, error message not displayed and the form was submitted')
            #driver.save_screenshot('./errormessage_testcase094_94 -03.png')
            return None

        self.driver.close()


    def test_chrome_095_95(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/en_ca/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

        # scroll to the form
        driver.execute_script("window.scrollTo(214,4760)")
        time.sleep(2)
        #driver.save_screenshot('./errormessage_testcase095_95 -01.png')

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('Viktor')  # Enter text

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('pofreussoummeva-1270@yopmail.com')  # Enter one blank space

        # No value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.click()

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('M5E 1E5')

        try:
            # check error message
            phonenum= driver.find_element(By.XPATH,
                                    "(//div[contains(.,'Please enter a phone number')])[12]")
            helpers.assert_subtitles('Please enter a phone number', phonenum)
            print("Test Case #095_95 passed \n")
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase095_95 -02.png')
        except Exception as e:
            print('Test #095-95 fail, error message not displayed')
            #driver.save_screenshot('./errormessage_testcase095_95 -03.png')
            return None

        self.driver.close()


    def test_chrome_096_96(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/en_ca/we-robot")
        delay()
        time.sleep(2)

        # click on Esc button to close overlay
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

        # scroll to the form
        driver.execute_script("window.scrollTo(214,4760)")
        time.sleep(2)
        driver.save_screenshot('./errormessage_testcase096_96 -01.png')

        # enter value into 'First Name' field
        first_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(first_input))
        first_input.clear()  # Clear field
        first_input.send_keys('Viktor')  # Enter text

        # enter value into 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # enter value into 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('pofreussoummeva-1270@yopmail.com')  # Enter one blank space

        # No value into 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(942) 368-2511')

        # enter value into 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('M5E 1E5')

        try:
            # check error message
            phonenum= driver.find_element(By.XPATH,
                                    "(//div[contains(.,'Please enter a valid phone number')])[12]")
            helpers.assert_subtitles('Please enter a valid phone number', phonenum)
            print("Test Case #096_96 passed \n")
            # error message screenshot
            #driver.save_screenshot('./errormessage_testcase096_96 -02.png')
        except Exception as e:
            print('Test #096-96 fail, error message not displayed')
            #driver.save_screenshot('./errormessage_testcase096_96 -03.png')
            return None

        self.driver.close()


    def tearDown(self):
        self.driver.quit()


    print("-------------------------------------TEST CASES FIREFOX---------------------------------- \n")

class FirefoxPositiveTests(unittest.TestCase):

    # The class setUp. I will have 3 (chrome,firefox,edge)
    def setUp(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        options.add_argument('--lang=en-US')
        options.page_load_strategy = 'eager'
        options.add_argument('--user-data-dir=/path/to/fresh/profile')
        # for Chrome setup , the 'service' was written as separate variable
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()


    def test_ff_090(self):
        driver = self.driver
        # opening Tesla website
        driver.get(helpers.main)
        delay()

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

        self.driver.close()
        print("Test Case #090 passed \n")

    def test_ff_091(self):
        driver = self.driver
        # opening 'We, Robot' page
        driver.get(helpers.mytestpage1)
        time.sleep(2)

        # checking for correct title in 'We, Robot' page
        assert "We, Robot | Tesla" in driver.title
        print("Title of 'We, Robot' page is correct")

        # Finding and clicking on 'Logo' link
        try:
            # clicking on 'Tesla' logo link
            werobot_link = WebDriverWait(driver, 2).until(EC.presence_of_element_located((
                By.XPATH, "//a[@aria-label='Tesla Logo']")))
            werobot_link.click()
            print("Tesla logo was clicked")
        except NoSuchElementException:
            print("No presence of 'Tesla' Logo on 'We, Robot' page")

        delay()

        # checking for 'We, Robot' page is open
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("The main page is open and title is correct")
        except NoSuchElementException:
            print("The main page is Not open")

        self.driver.close()
        print("Test Case #091 passed \n")

    def test_ff_092(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(1)

        # click on Esc button to close overlay
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        # check WE ROBOT image
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@class='tds-icon tds-icon-logo-we-robot-alt']")))
            print("WE, ROBOT image was found")
        except NoSuchElementException:
            print("WE, ROBOT image was not found")

        futureautonomus = driver.find_element(By.XPATH, "// h2[contains(., 'The Future Is Autonomous')]")
        helpers.assert_subtitles('The Future Is Autonomous', futureautonomus)
        # check if iframe with video exists
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "twitter-widget-0")))
            print("iframe with video for ‘The Future Is Autonomous’ exits")
        except NoSuchElementException:
            print("iframe with video for ‘The Future Is Autonomous’ not found")

        autonomy = driver.find_element(By.XPATH, " //h2[contains(.,'Autonomy for All')]")
        helpers.assert_subtitles('Autonomy for All', autonomy)

        robotaxi = driver.find_element(By.XPATH, "//span[contains(., 'Robotaxi')]")
        helpers.assert_subtitles('Robotaxi', robotaxi)
        # check Robotaxi image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt = 'Robotaxi']")))
            print("Image for ‘Robotaxi’ was found")
        except NoSuchElementException:
            print("Image for ‘Robotaxi’ was Not found")

        robovan = driver.find_element(By.XPATH, "//span[contains(.,'Robovan')]")
        helpers.assert_subtitles('Robovan', robovan)
        # check Robovan image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Robovan']")))
            print("Image for ‘Robovan’ was found")
        except NoSuchElementException:
            print("Image for ‘Robovan’ was Not found")

        teslabot = driver.find_element(By.XPATH, "//span[contains(.,'Tesla Bot')]")
        helpers.assert_subtitles('Tesla Bot', teslabot)
        # check Tesla Bot image
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Optimus']")))
            print("Image for ‘Tesla Bot’ was found")
        except NoSuchElementException:
            print("Image for ‘Tesla Bot’ was Not found")

        autonomy2 = driver.find_element(By.XPATH, "(//span[contains(.,'Discover Autonomy')])[2]")
        helpers.assert_subtitles('Discover Autonomy', autonomy2)
        # check Discover Autonomy video
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "tesla-video-4261")))
            print("Video for 'Discover Autonomy' was found")
        except NoSuchElementException:
            print("Video for 'Discover Autonomy' was Not found")
        # check Discover Autonomy form
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, "tesla-form-standalone-1546")))
            print("Form for 'Discover Autonomy' was found")
        except NoSuchElementException:
            print("Form for 'Discover Autonomy' was Not found")

        futureautonomus2 = driver.find_element(By.XPATH, "//h1[contains(.,'The Future is Autonomous')] ")
        helpers.assert_subtitles('The Future is Autonomous', futureautonomus2)
        # check subtitle
        futureautonomussub = driver.find_element(By.XPATH,
                                                 "//p[contains(.,'Experience Full Self-Driving (Supervised) in any Tesla vehicle with a demo drive.')]")
        helpers.assert_subtitles('Experience Full Self-Driving (Supervised) in any Tesla vehicle with a demo drive.',
                                 futureautonomussub)
        # check image ‘The Future Is Autonomous’ at the bottom page
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dx-end-content']")))
            print("Image for ‘The Future Is Autonomous’ was found")
        except NoSuchElementException:
            print("Image for ‘The Future Is Autonomous’ was Not found")

        # check button 'Experience Tesla' at the bottom page
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Experience Tesla')]")))
            print("Button 'Experience Tesla' was found")
        except NoSuchElementException:
            print("IButton 'Experience Tesla' was Not found")

        self.driver.close()
        print("Test Case #092 passed \n")

    def test_ff_093(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(1)

        # click on Esc button to close overlay
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(3)

        # Store the ID of the original window
        original_window = driver.current_window_handle
        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1

        # variant 1 :
        # Finding and clicking on the link 'Watch on X/Continue watching on X' inside the iframe

        # scroll to the link  'Watch on X/Continue watching on X' was visible
        driver.execute_script("window.scrollTo(0,600)")

        # wait iframe and switch to
        iframewathch = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,
                                                                                      "twitter-widget-0")))
        driver.switch_to.frame(iframewathch)
        print("Swith to iFrame done")
        delay()

        try:
            #  click on link open new Tab
            driver.find_element(By.XPATH, "(//a[starts-with(@href, 'https://twitter.com/Tesla/status/')])[2]").click()
            print("The link 'Continue watching on X/Watch on X' was clicked")
        except NoSuchElementException:
            print("The link 'Continue watching on X/Watch on X' was not clicked")

        # Wait for the new tab
        WebDriverWait(driver, 1).until(EC.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        print("Switch to new tab done")
        time.sleep(4)
        # print(driver.title)

        try:
            # assert the title of the 'X' page is being open
            assert 'Tesla on X: "The future will be streamed live 10/10, 7pm PT https://t.co/YJEjZIYoTA" / X' in driver.title
            print("The new Tesla page in 'X' is open and the title is correct")
        except NoSuchElementException:
            print("The new Tesla page in 'X' is not open")

        # Switch back to the old tab or window
        driver.switch_to.window(original_window)

        '''
        # variant 2 : open X page with direct URL  instead of  clicking link 'Continue watching on X'

        # Opens a new tab and switches to new tab
        driver.switch_to.new_window('tab')

        # Load a new 'X' page
        driver.get(
            "https://twitter.com/Tesla/status/1843922599765590148?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1843922599765590148%7Ctwgr%5Eedc586053e267ec694fe0d2d476dec65c7865714%7Ctwcon%5Es1_&amp;ref_url=https%3A%2F%2Fwww.tesla.com%2Fen_ca%2Fwe-robot")

        try:
            # Wait for the new tab to finish loading content
            WebDriverWait(driver, 3).until(EC.title_contains('Tesla on X: "The future will be streamed live '))
            print("The new Tesla page in 'X' is open and the title is: \n" + driver.title)
        except NoSuchElementException:
            print("The new Tesla page in 'X' is not open")
        '''

        self.driver.close()
        print("Test Case #093 passed \n")

    def test_ff_094(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(1)

        # click on Esc button to close overlay
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0,2400)")
        time.sleep(3)

        # click on Robotaxi text
        driver.find_element(By.XPATH, "//span[contains(., 'Robotaxi')]").click()
        # check Robotaxi image open
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt = 'Robotaxi']")))
            print("Image for ‘Robotaxi’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Robotaxi’ was Not  displayed")

        # click on Robovan text
        driver.find_element(By.XPATH, "//span[contains(.,'Robovan')]").click()
        # check Robovan image open
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Robovan']")))
            print("Image for ‘Robovan’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Robovan’ was Not displayed")

        # click on Tesla Bot text
        driver.find_element(By.XPATH, "//span[contains(.,'Tesla Bot')]").click()
        # check Tesla Bot image open
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Optimus']")))
            print("Image for ‘Tesla Bot’ was displayed")
        except NoSuchElementException:
            print("Image for ‘Tesla Bot’ was Not displayed")

        self.driver.close()
        print("Test Case #094 passed \n")

    def test_ff_095(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(1)

        # click on Esc button to close overlay
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        # check 'First Name' title
        firstname = driver.find_element(By.XPATH, "//label[contains(.,'First Name')]")
        helpers.assert_subtitles('First Name', firstname)

        # check 'Last Name' title
        lastname = driver.find_element(By.XPATH, "//label[contains(.,'Last Name')]")
        helpers.assert_subtitles('Last Name', lastname)

        # check 'Email Address' title
        emailaddress = driver.find_element(By.XPATH, "//label[contains(.,'Email Address')]")
        helpers.assert_subtitles('Email Address', emailaddress)

        # check 'Phone Number' title
        phonenum = driver.find_element(By.XPATH, "//label[contains(.,'Phone Number')]")
        helpers.assert_subtitles('Phone Number', phonenum)

        # check 'Zip Code' title
        zipcode = driver.find_element(By.XPATH, "//label[contains(.,'Zip Code')]")
        helpers.assert_subtitles('Zip Code', zipcode)

        # click on the 'First Name' field and Enter, for all fields be clicked on one time
        # ...
        # check_input.send_keys(Keys.ENTER)
        #  all fields clicked screenshot
        # driver.save_screenshot('./image.png')

        # scroll to the First Name field with offset
        driver.execute_script("window.scrollTo(214,3160)")
        time.sleep(3)

        # move to First Name field
        action_first = ActionChains(driver)
        check_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//input[@name='firstName']")))
        driver.save_full_page_screenshot('./errormessage_testcaseff096_1.png')
        # clear field
        check_input.clear()
        # click on field
        action_first.move_to_element(check_input).click().perform()

        # click on title , for error message be appeared
        firstname.click()
        # check error message
        firstmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[1]")
        helpers.assert_subtitles('Required', firstmessage)

        # click on the 'Last Name' field
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        lastname.click()
        # check error message
        lastmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[2]")
        helpers.assert_subtitles('Required', lastmessage)

        # click on the 'Email Address' field
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        emailaddress.click()
        # check error message
        emailmessage = driver.find_element(By.XPATH, "(//div[@class='tds-form-feedback-text'][text()='Required'])[3]")
        helpers.assert_subtitles('Required', emailmessage)

        # click on the 'Phone Number' field
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        phonenum.click()
        # check error message
        phonemessage = driver.find_element(By.XPATH, "//div[text()='Please enter a phone number']")
        helpers.assert_subtitles('Please enter a phone number', phonemessage)

        # click on the 'Zip Code' field
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.click()
        # click on title , for error message be appeared
        zipcode.click()
        # check error message
        zipmessage = driver.find_element(By.XPATH, "//div[@class='tds-form-feedback-text'][text()='Invalid']")
        helpers.assert_subtitles('Invalid', zipmessage)

        self.driver.close()
        print("Test Case #095 passed \n")


    def test_ff_096(self):
        driver = self.driver

        # opening 'We, Robot' page
        driver.get("https://www.tesla.com/we-robot")
        delay()
        time.sleep(1)

        # click on Esc button to close overlay
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        # scroll to the First Name field
        driver.execute_script("window.scrollTo(214,3160)")
        time.sleep(3)

        # move to First Name field
        action_first = ActionChains(driver)
        check_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//input[@name='firstName']")))
        # clear field
        check_input.clear()

        # move to the First Name field with offset to avoid banner's overlay and enter value
        #action_first.move_to_element_with_offset(check_input, 0, -20).send_keys('Viktor').perform()
        # move to the First Name field  and enter value
        #action_first.move_to_element(check_input).send_keys('Viktor').perform()
        action_first.move_to_element(check_input).perform()
        check_input.send_keys('Viktor')
        # screen this
        driver.save_full_page_screenshot('./errormessage_testcaseff096_1.png')

        # click on the 'Last Name' field and enter value
        check_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
        check_input.clear()  # Clear field
        check_input.send_keys('Keytest')

        # click on the 'Email Address' field and enter value
        check_input = driver.find_element(By.XPATH, "//input[@name='email']")
        check_input.clear()  # Clear field
        check_input.send_keys('xudeimmidduco-2654@yopmail.com')  # Enter text

        # click on the 'Phone Number' field and enter value
        check_input = driver.find_element(By.XPATH, "//input[@ name='phone']")
        check_input.clear()  # Clear field
        check_input.send_keys('(415) 555-1234')  # Enter text

        # click on the 'Zip Code' field and enter value
        check_input = driver.find_element(By.XPATH, "//input[@name='zip']")
        check_input.clear()  # Clear field
        check_input.send_keys('94111')  # Enter text
        delay()

        try:
            # click on Submit button
            submitbut = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(.,'Submit')]")))
            # driver.execute_script('arguments[0].scrollIntoView()', submitbut)
            #print( submitbut.location)
            submitbut.click()
            print('Submit button was clicked')

            WebDriverWait(driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(.,'Thank you')]")))
            print("Test Case #096 passed \n")

        except Exception as e:
            # print error message
            print('Test #096 fail, something went wrong')
            # error message screenshot
            driver.save_full_page_screenshot('./errormessage_testcaseff096_2.png')
            return None

        self.driver.close()

    def tearDown(self):
        self.driver.quit()

    print("-------------------------------------NEGATIVE TEST CASES FIREFOX---------------------------------- \n")

