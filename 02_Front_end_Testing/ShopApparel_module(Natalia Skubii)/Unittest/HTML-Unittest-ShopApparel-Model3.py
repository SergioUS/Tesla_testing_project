# Unittest, includes Positive and Negative tests for Tesla site, Shop Apparel and Model 3 modules(prepared by Natalia Skubii)
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options
import HelpersShopApparelModel3 as H
import HtmlTestRunner
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(1,5))

class ChromePositiveNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()


    def test_case_026(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(APPAREL-MODEL 3)                                  ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_026
        print("                                                                                                    ")
        print("             Apparel test_case_026                                                                  ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)


        #Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        # Check if the new window title contains "Apparel"
        if "Apparel" not in driver.title:
            raise Exception("Apparel - Test Case 026 failed")
        else:
            print("Apparel is available - Test Case 026 passed")

        # Test results for test_case_26
        print("                                                                                                    ")
        print("        !!!  test_case_026  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")


    def test_case_027(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_027                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        # Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        #Click on the button "Built for Any Planet Trucker Hat"
        driver.find_element(By.XPATH, H.hat_link).click()


        #Click on the button "Email me when this item is restocked"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.emailRestoked_link))).click()

        #Enter incorrect email domain
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.input_email_link)))
        email_input.send_keys("test@incorrect_domain")

        #Click on the button "Notify me"
        notify_button = driver.find_element(By.XPATH, H.notify_button)
        notify_button.click()

        # Verify that an error message or validation occurs due to the incorrect email domain

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.invalid_email_error)))

        if error_message:
            print("Error message displayed as expected - Test Case 027 passed")
        else:
            print("No error message displayed - Test Case 027 failed")
            self.fail("No error message was shown for the incorrect email domain")

        # Test results for test_case_027
        print("                                                                                                   ")
        print("        !!!  test_case_027  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_028(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_028                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        delay()

        # Navigate on the Apparel link and click on the Men - Tees link
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
                var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                arguments[0].dispatchEvent(event);
                """
        driver.execute_script(hover_script, apparel)
        delay()
        tees = driver.find_element(By.XPATH, H.tees)
        action = ActionChains(driver)
        action.move_to_element(tees).click().perform()
        delay()

        #Click on the link "Men's Cybertruck Cityscape Tee"
        driver.find_element(By.XPATH, H.partial_link).click()
        delay()

        #Choose an available size ("S", "M", "L", "XL", "XXL")
        #driver.find_element(By.XPATH, H.size_S).click()
        driver.find_element(By.XPATH, H.size_M).click()
        #driver.find_element(By.XPATH, H.size_L).click()
        #driver.find_element(By.XPATH, H.size_XL).click()
        #driver.find_element(By.XPATH, H.size_XXL).click()

        delay()

        #Choose quantity (1)
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
             print("Add to cart page is visible - Test Case 028 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 028 failed")

        # Test results for test_case_028
        print("                                                                                                   ")
        print("        !!!  test_case_028  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_029(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        MODEL 3 test_case_029                                                                        ")
        print("        --------------------                                                                         ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        #Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        #Click on the "Order" button for Model 3
        order_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_button)))
        order_button.click()


        page_order = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_order)))
        page_order.click()
        WebDriverWait(driver, 5)

        # Verify Model 3 slide
        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()
        print("----Right scroll 4 times completed")

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)
        print("----Left scroll 4 times completed")

        # Test results for test_case_029
        print("                                                                                                   ")
        print("        !!!  test_case_029  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_030(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_030                                                                        ")
        print("        --------------------                                                                         ")


        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        #Navigate on the Apparel link and click on the Onesies button
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
        arguments[0].dispatchEvent(event);
        """
        driver.execute_script(hover_script, apparel)
        delay()
        onesies = driver.find_element(By.XPATH, H.onesie)
        action = ActionChains(driver)
        action.move_to_element(onesies).click().perform()
        delay()

        #Click on the Scribble T Logo Onesie link
        scribble_onesie = driver.find_element(By.XPATH, H.scribble_onesie)
        scribble_onesie.click()
        WebDriverWait(driver, 5)

        # Choose the color "Gray"
        gray_color_button = driver.find_element(By.XPATH, H.gray_color)
        gray_color_button.click()
        time.sleep(3)

        # Choose size "6"
        size_6_button = driver.find_element(By.XPATH, H.size_6)
        size_6_button.click()
        time.sleep(3)

        # Choose quantity 1
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input1)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart1)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart1)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
            print("Add to cart page is visible - Test Case 030 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 030 failed")

        # Test results for test_case_030
        print("                                                                                                  ")
        print("        !!!  test_case_030  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_026_26(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(MODEL 3)                                          ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

      # test_case_026_26
        print("                                                                                                    ")
        print("             MODEL 3 test_case_026_26                                                               ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)


        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        #Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        delay()

        #Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

        #Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")

        #Enter Phone number
        phone_number = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone_number.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)


        #Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        #Verify that an error message or validation occurs due to the not entered First name
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message1)))

        if error_message:
            print("Error message displayed as expected - Test Case 026_26 passed")
        else:
            print("No error message displayed - Test Case 026_26 failed")
            self.fail("No error message was shown when no First name was entered")

        # Test results for test_case_026_26
        print("                                                                                                  ")
        print("        !!!  test_case_026_26  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_027_27(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_027_27                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        #Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")


        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

        # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        # Verify that an error message or validation occurs due to the not entered phone number

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message2)))

        if error_message:
            print("Error message displayed as expected - Test Case 027_27 passed")
        else:
            print("No error message displayed - Test Case 027_27 failed")
            self.fail("No error message was shown when no phone number was entered")

        # Test results for test_case_027_27
        print("                                                                                                  ")
        print("        !!!  test_case_027_27  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_028_28(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_028_28                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()


        # Find and click on the button "Order" Model 3
        order = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order)))
        order.click()
        delay()

        #Click on the button "Lease"
        lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.lease)))
        lease.click()


        #Click on the button "Order now"
        order_lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_lease)))
        order_lease.click()
        delay()

        #Click on the button "Order with Card"
        order_card = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_card)))
        order_card.click()

        #Enter First name in Account Details
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name_account)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name_account)))
        last_name.send_keys("Smith")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_account)))
        email_address.send_keys("pacara4727@eachart.com")


        #Enter Confirm email address
        confirm_account = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.confirm_account)))
        confirm_account.send_keys("pacara4727@eacart.com")
        delay()

        # Verify that an error message or validation is triggered when an incorrect email address is entered
        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message3)))

        if error_message:
            print("Error message displayed as expected - Test Case 028_28 passed")
        else:
            print("No error message displayed - Test Case 028_28 failed")
            self.fail("No error message was displayed when an incorrect email address was entered")

        # Test results for test_case_028_28
        print("                                                                                                  ")
        print("        !!!  test_case_028_28  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_029_29(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_029_29                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("&&&$$$123")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")


        #Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

       # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        if last_name:
            print("WARNING! Test Case 029_29 failed!")

        else:
            print("No access granted with wrong Last name - Test Case 029_29 passed")

        # Test results for test_case_029_29
        print("                                                                                                  ")
        print("        !!!  test_case_029_29  FAIL   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_030_30(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_030_30                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

       #Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

       # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

# Verify that an error message or validation is triggered when no email address is entered
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message4)))

        if error_message:
            print("Error message displayed as expected - Test Case 030_30 passed")
        else:
            print("No error message displayed - Test Case 030_30 failed")
            self.fail("No error message was displayed when no email address was entered")

            # Test results for test_case_030_30
        print("                                                                                                  ")
        print("        !!!  test_case_030_30  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def tearDown(self):
        self.driver.quit()
class EdgePositiveNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()

    def test_case_026(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(APPAREL-MODEL 3)                                  ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_026
        print("                                                                                                    ")
        print("             Apparel test_case_026                                                                  ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        H.moving_to_new_window(driver)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)


        #Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        # Check if the new window title contains "Apparel"
        if "Apparel" not in driver.title:
            raise Exception("Apparel - Test Case 026 failed")
        else:
            print("Apparel is available - Test Case 026 passed")

        # Test results for test_case_26
        print("                                                                                                    ")
        print("        !!!  test_case_026  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")

    def test_case_027(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_027                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        # Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        #Click on the button "Built for Any Planet Trucker Hat"
        driver.find_element(By.XPATH, H.hat_link).click()


        #Click on the button "Email me when this item is restocked"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.emailRestoked_link))).click()

        #Enter incorrect email domain
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.input_email_link)))
        email_input.send_keys("test@incorrect_domain")

        #Click on the button "Notify me"
        notify_button = driver.find_element(By.XPATH, H.notify_button)
        notify_button.click()

        # Verify that an error message or validation occurs due to the incorrect email domain

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.invalid_email_error)))

        if error_message:
            print("Error message displayed as expected - Test Case 027 passed")
        else:
            print("No error message displayed - Test Case 027 failed")
            self.fail("No error message was shown for the incorrect email domain")

        # Test results for test_case_027
        print("                                                                                                   ")
        print("        !!!  test_case_027  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_028(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_028                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        delay()

        # Navigate on the Apparel link and click on the Men - Tees link
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
                var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                arguments[0].dispatchEvent(event);
                """
        driver.execute_script(hover_script, apparel)
        delay()
        tees = driver.find_element(By.XPATH, H.tees)
        action = ActionChains(driver)
        action.move_to_element(tees).click().perform()
        delay()

        #Click on the link "Men's Cybertruck Cityscape Tee"
        driver.find_element(By.XPATH, H.partial_link).click()
        delay()

        #Choose an available size ("S", "M", "L", "XL", "XXL")
        #driver.find_element(By.XPATH, H.size_S).click()
        driver.find_element(By.XPATH, H.size_M).click()
        #driver.find_element(By.XPATH, H.size_L).click()
        #driver.find_element(By.XPATH, H.size_XL).click()
        #driver.find_element(By.XPATH, H.size_XXL).click()

        delay()

        #Choose quantity (1)
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
             print("Add to cart page is visible - Test Case 028 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 028 failed")

        # Test results for test_case_028
        print("                                                                                                   ")
        print("        !!!  test_case_028  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_029(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        MODEL 3 test_case_029                                                                        ")
        print("        --------------------                                                                         ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        #Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        #Click on the "Order" button for Model 3
        order_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_button)))
        order_button.click()


        page_order = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_order)))
        page_order.click()
        WebDriverWait(driver, 5)

        # Verify Model 3 slide
        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()
        print("----Right scroll 4 times completed")

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)
        print("----Left scroll 4 times completed")

        # Test results for test_case_029
        print("                                                                                                   ")
        print("        !!!  test_case_029  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_030(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_030                                                                        ")
        print("        --------------------                                                                         ")


        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        #Navigate on the Apparel link and click on the Onesies button
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
        arguments[0].dispatchEvent(event);
        """
        driver.execute_script(hover_script, apparel)
        delay()
        onesies = driver.find_element(By.XPATH, H.onesie)
        action = ActionChains(driver)
        action.move_to_element(onesies).click().perform()
        delay()

        #Click on the Scribble T Logo Onesie link
        scribble_onesie = driver.find_element(By.XPATH, H.scribble_onesie)
        scribble_onesie.click()
        WebDriverWait(driver, 5)

        # Choose the color "Gray"
        gray_color_button = driver.find_element(By.XPATH, H.gray_color)
        gray_color_button.click()
        time.sleep(3)

        # Choose size "6"
        size_6_button = driver.find_element(By.XPATH, H.size_6)
        size_6_button.click()
        time.sleep(3)

        # Choose quantity 1
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input1)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart1)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart1)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
            print("Add to cart page is visible - Test Case 030 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 030 failed")

        # Test results for test_case_030
        print("                                                                                                  ")
        print("        !!!  test_case_030  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_026_26(self):
        driver = self.driver
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(MODEL 3)                                          ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

      # test_case_026_26
        print("                                                                                                    ")
        print("             MODEL 3 test_case_026_26                                                               ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        #Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)

        #Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

        #Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")

        #Enter Phone number
        phone_number = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone_number.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()


        #Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        #Verify that an error message or validation occurs due to the not entered First name
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message1)))

        if error_message:
            print("Error message displayed as expected - Test Case 026_26 passed")
        else:
            print("No error message displayed - Test Case 026_26 failed")
            self.fail("No error message was shown when no First name was entered")

        # Test results for test_case_026_26
        print("                                                                                                  ")
        print("        !!!  test_case_026_26  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_027_27(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_027_27                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)

        #Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")


        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

        # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        # Verify that an error message or validation occurs due to the not entered phone number

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message2)))

        if error_message:
            print("Error message displayed as expected - Test Case 027_27 passed")
        else:
            print("No error message displayed - Test Case 027_27 failed")
            self.fail("No error message was shown when no phone number was entered")

        # Test results for test_case_027_27
        print("                                                                                                  ")
        print("        !!!  test_case_027_27  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_028_28(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_028_28                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()


        # Find and click on the button "Order" Model 3
        order = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order)))
        order.click()
        delay()

        #Click on the button "Lease"
        lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.lease)))
        lease.click()


        #Click on the button "Order now"
        order_lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_lease)))
        order_lease.click()
        delay()

        #Click on the button "Order with Card"
        order_card = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_card)))
        order_card.click()

        #Enter First name in Account Details
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name_account)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name_account)))
        last_name.send_keys("Smith")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_account)))
        email_address.send_keys("pacara4727@eachart.com")


        #Enter Confirm email address
        confirm_account = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.confirm_account)))
        confirm_account.send_keys("pacara4727@eacart.com")
        delay()

        # Verify that an error message or validation is triggered when an incorrect email address is entered
        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message3)))

        if error_message:
            print("Error message displayed as expected - Test Case 028_28 passed")
        else:
            print("No error message displayed - Test Case 028_28 failed")
            self.fail("No error message was displayed when an incorrect email address was entered")

        # Test results for test_case_028_28
        print("                                                                                                  ")
        print("        !!!  test_case_028_28  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_029_29(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_029_29                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("&&&$$$123")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")


        #Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

       # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        if last_name:
            print("WARNING! Test Case 029_29 failed!")

        else:
            print("No access granted with wrong Last name - Test Case 029_29 passed")

        # Test results for test_case_029_29
        print("                                                                                                  ")
        print("        !!!  test_case_029_29  FAIL   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_030_30(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_030_30                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

       #Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

       # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

# Verify that an error message or validation is triggered when no email address is entered
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message4)))

        if error_message:
            print("Error message displayed as expected - Test Case 030_30 passed")
        else:
            print("No error message displayed - Test Case 030_30 failed")
            self.fail("No error message was displayed when no email address was entered")

            # Test results for test_case_030_30
        print("                                                                                                  ")
        print("        !!!  test_case_030_30  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def tearDown(self):
        self.driver.quit()
class FireFoxPositiveNegativeTestCases(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()

        # Set preferences to allow geolocation
        profile.set_preference("geo.prompt.testing", True)
        profile.set_preference("geo.prompt.testing.allow", True)
        profile.set_preference("geo.enabled", True)
        profile.set_preference("geo.provider.use_corelocation", True)
        profile.set_preference("geo.provider.use_gpsd", False)
        profile.set_preference("geo.wifi.uri",
                               "data:application/json,{\"location\": {\"lat\": 50.455755, \"lng\": 30.511565}, \"accuracy\": 100.0}")

        # Set up Firefox options
        options = Options()
        options.profile = profile

        # Use WebDriverManager to manage the Firefox driver
        service = FirefoxService(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()


    def test_case_026(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(APPAREL-MODEL 3)                                  ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_026
        print("                                                                                                    ")
        print("             Apparel test_case_026                                                                  ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)


        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)


        #Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        # Check if the new window title contains "Apparel"
        if "Apparel" not in driver.title:
            raise Exception("Apparel - Test Case 026 failed")
        else:
            print("Apparel is available - Test Case 026 passed")

        # Test results for test_case_26
        print("                                                                                                    ")
        print("        !!!  test_case_026  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")

    def test_case_027(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_027                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        # Click on the header menu "Apparel"
        apparel_menu = driver.find_element(By.XPATH, H.apparel_link)
        apparel_menu.click()
        time.sleep(3)

        #Click on the button "Built for Any Planet Trucker Hat"
        driver.find_element(By.XPATH, H.hat_link).click()


        #Click on the button "Email me when this item is restocked"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.emailRestoked_link))).click()

        #Enter incorrect email domain
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.input_email_link)))
        email_input.send_keys("test@incorrect_domain")

        #Click on the button "Notify me"
        notify_button = driver.find_element(By.XPATH, H.notify_button)
        notify_button.click()

        # Verify that an error message or validation occurs due to the incorrect email domain

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.invalid_email_error)))

        if error_message:
            print("Error message displayed as expected - Test Case 027 passed")
        else:
            print("No error message displayed - Test Case 027 failed")
            self.fail("No error message was shown for the incorrect email domain")

        # Test results for test_case_027
        print("                                                                                                   ")
        print("        !!!  test_case_027  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_028(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_028                                                                        ")
        print("        --------------------                                                                         ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        # Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(5)

        # Navigate on the Apparel link and click on the Men - Tees link
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
                var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                arguments[0].dispatchEvent(event);
                """
        driver.execute_script(hover_script, apparel)
        delay()
        tees = driver.find_element(By.XPATH, H.tees)
        action = ActionChains(driver)
        action.move_to_element(tees).click().perform()
        time.sleep(5)

        #Click on the link "Men's Cybertruck Cityscape Tee"
        driver.find_element(By.XPATH, H.partial_link).click()
        delay()

        #Choose an available size ("S", "M", "L", "XL", "XXL")
        #driver.find_element(By.XPATH, H.size_S).click()
        driver.find_element(By.XPATH, H.size_M).click()
        #driver.find_element(By.XPATH, H.size_L).click()
        #driver.find_element(By.XPATH, H.size_XL).click()
        #driver.find_element(By.XPATH, H.size_XXL).click()

        delay()

        #Choose quantity (1)
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
             print("Add to cart page is visible - Test Case 028 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 028 failed")

        # Test results for test_case_028
        print("                                                                                                   ")
        print("        !!!  test_case_028  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_029(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        MODEL 3 test_case_029                                                                        ")
        print("        --------------------                                                                         ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        #Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        #Click on the "Order" button for Model 3
        order_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_button)))
        order_button.click()


        page_order = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_order)))
        page_order.click()
        WebDriverWait(driver, 5)

        # Verify Model 3 slide
        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()

        driver.find_element(By.XPATH, H.right_carousel).click()
        delay()
        print("----Right scroll 4 times completed")

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)

        driver.find_element(By.XPATH, H.left_carousel).click()
        time.sleep(2)
        print("----Left scroll 4 times completed")

        # Test results for test_case_029
        print("                                                                                                   ")
        print("        !!!  test_case_029  PASS   !!!                                                             ")
        print("         -----------------------------                                                             ")

    def test_case_030(self):
        driver = self.driver
        print("                                                                                                     ")
        print("        APPAREL test_case_030                                                                        ")
        print("        --------------------                                                                         ")


        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        #Click on the header menu "Shop"
        shop_menu = driver.find_element(By.XPATH, H.shop_link)
        shop_menu.click()
        time.sleep(3)

        #Navigate on the Apparel link and click on the Onesies button
        apparel = driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[1]/ol/li[3]/div')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of(apparel))
        actions = ActionChains(driver)
        actions.move_to_element(apparel).perform()
        hover_script = """
        var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
        arguments[0].dispatchEvent(event);
        """
        driver.execute_script(hover_script, apparel)
        delay()
        onesies = driver.find_element(By.XPATH, H.onesie)
        action = ActionChains(driver)
        action.move_to_element(onesies).click().perform()
        delay()

        #Click on the Scribble T Logo Onesie link
        scribble_onesie = driver.find_element(By.XPATH, H.scribble_onesie)
        scribble_onesie.click()
        WebDriverWait(driver, 5)

        # Choose the color "Gray"
        gray_color_button = driver.find_element(By.XPATH, H.gray_color)
        gray_color_button.click()
        time.sleep(3)

        # Choose size "6"
        size_6_button = driver.find_element(By.XPATH, H.size_6)
        size_6_button.click()
        time.sleep(3)

        # Choose quantity 1
        quantity_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.quantity_input1)))
        quantity_input.clear()
        quantity_input.send_keys("1")
        delay()

        add_to_cart = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.add_to_cart1)))
        add_to_cart.click()
        delay()

        add_to_cart_page = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.page_cart1)))

        # Assert that the add to cart page element is displayed
        self.assertTrue(add_to_cart_page.is_displayed(), "Add to Cart page not displayed")
        if add_to_cart_page.is_displayed():
            print("Add to cart page is visible - Test Case 030 passed")
        else:
            raise Exception("Add to cart page is not visible - Test Case 030 failed")

        # Test results for test_case_030
        print("                                                                                                  ")
        print("        !!!  test_case_030  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_026_26(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          TESLA--(MODEL 3)                                          ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

      # test_case_026_26
        print("                                                                                                    ")
        print("             MODEL 3 test_case_026_26                                                               ")
        print("             ------------------------                                                               ")

        #Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        #Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        time.sleep(6)

        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        time.sleep(5)

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        delay()

        #Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

        #Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")

        #Enter Phone number
        phone_number = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone_number.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()


        #Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        #Verify that an error message or validation occurs due to the not entered First name
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message1)))

        if error_message:
            print("Error message displayed as expected - Test Case 026_26 passed")
        else:
            print("No error message displayed - Test Case 026_26 failed")
            self.fail("No error message was shown when no First name was entered")

        # Test results for test_case_026_26
        print("                                                                                                  ")
        print("        !!!  test_case_026_26  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_027_27(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_027_27                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        #Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")


        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

        # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        # Verify that an error message or validation occurs due to the not entered phone number

        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message2)))

        if error_message:
            print("Error message displayed as expected - Test Case 027_27 passed")
        else:
            print("No error message displayed - Test Case 027_27 failed")
            self.fail("No error message was shown when no phone number was entered")

        # Test results for test_case_027_27
        print("                                                                                                  ")
        print("        !!!  test_case_027_27  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_028_28(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_028_28                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()


        # Find and click on the button "Order" Model 3
        order = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order)))
        order.click()
        delay()

        #Click on the button "Lease"
        lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.lease)))
        lease.click()


        #Click on the button "Order now"
        order_lease = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_lease)))
        order_lease.click()
        time.sleep(5)

        #Click on the button "Order with Card"
        order_card = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.order_card)))
        order_card.click()

        #Enter First name in Account Details
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name_account)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name_account)))
        last_name.send_keys("Smith")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_account)))
        email_address.send_keys("pacara4727@eachart.com")


        #Enter Confirm email address
        confirm_account = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.confirm_account)))
        confirm_account.send_keys("pacara4727@eacart.com")
        delay()

        # Verify that an error message or validation is triggered when an incorrect email address is entered
        error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message3)))

        if error_message:
            print("Error message displayed as expected - Test Case 028_28 passed")
        else:
            print("No error message displayed - Test Case 028_28 failed")
            self.fail("No error message was displayed when an incorrect email address was entered")

        # Test results for test_case_028_28
        print("                                                                                                  ")
        print("        !!!  test_case_028_28  PASS   !!!                                                            ")
        print("         -----------------------------                                                            ")

    def test_case_029_29(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_029_29                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(5)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        delay()

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("&&&$$$123")

        # Enter Email address
        email_address = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.email_address)))
        email_address.send_keys("pacara4727@eachart.com")

        # Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

        # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

        if last_name:
            print("WARNING! Test Case 029_29 failed!")

        else:
            print("No access granted with wrong Last name - Test Case 029_29 passed")

        # Test results for test_case_029_29
        print("                                                                                                  ")
        print("        !!!  test_case_029_29  FAIL   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def test_case_030_30(self):
        driver = self.driver
        print("                                                                                                    ")
        print("             MODEL 3 test_case_030_30                                                               ")
        print("             ------------------------                                                               ")

        # Go to https://www.tesla.com/
        driver.get(H.tesla_url)
        time.sleep(3)

        # Click on the header menu "Vehicles"
        vehicles_menu = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.vehicles_link)))
        vehicles_menu.click()

        # Click on the "Learn" link for Model 3
        learn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn)))
        learn.click()

        # Click on the button "Learn more"
        learn_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.learn_more)))
        learn_more.click()
        time.sleep(5)

        # Find and click on the button "Experience Model 3"
        driver.find_element(By.XPATH, H.experience)

        experience = driver.switch_to.active_element
        experience.send_keys(Keys.PAGE_DOWN)

        experience = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, H.experience)))
        experience.click()
        delay()

        driver.find_element(By.XPATH, H.last_name)

        last_name = driver.switch_to.active_element
        last_name.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        # Enter First name
        first_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.first_name)))
        first_name.send_keys("John")

        # Enter Last name
        last_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.last_name)))
        last_name.send_keys("Smith")

       #Enter Phone number
        phone = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.phone)))
        phone.send_keys("7175555555")
        delay()

        driver.find_element(By.XPATH, H.submit)

        submit = driver.switch_to.active_element
        submit.send_keys(Keys.PAGE_DOWN)
        delay()

       # Click on the button "Submit"
        submit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, H.submit)))
        submit.click()

# Verify that an error message or validation is triggered when no email address is entered
        error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, H.error_message4)))

        if error_message:
            print("Error message displayed as expected - Test Case 030_30 passed")
        else:
            print("No error message displayed - Test Case 030_30 failed")
            self.fail("No error message was displayed when no email address was entered")

            # Test results for test_case_030_30

        print("                                                                                                  ")
        print("        !!!  test_case_030_30  PASS   !!!                                                         ")
        print("         -----------------------------                                                            ")

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
     suite = unittest.TestSuite()
     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ChromePositiveNegativeTestCases))
     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EdgePositiveNegativeTestCases))
     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(FireFoxPositiveNegativeTestCases))
     runner = HtmlTestRunner.HTMLTestRunner(
         output='C:/Users/natal/PycharmProjects/Tesla_testing_project/02_Front_end_Testing/ShopApparel_module(Natalia Skubii)/HTML_Report')
     runner.run(suite)
