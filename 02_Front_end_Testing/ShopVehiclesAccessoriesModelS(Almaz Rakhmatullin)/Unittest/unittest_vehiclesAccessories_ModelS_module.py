import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import helpers
from helpers import (loc_shop, loc_modelS, loc_good1, loc_plus_quantity,
                     loc_input_field, loc_add_cart, loc_view_cart, loc_remove, loc_remove_accept,
                     loc_select_amount, loc_select2, loc_search, loc_search_field, loc_search_result, loc_out_of_stock,
                     loc_good1_price, loc_good1_price_cart, loc_empty_cart, name_good,
                     loc_search_result1, loc_search_result_empty, loc_vehicle_acc1,
                     loc_vehicle_acc2, amount1, amount2, loc_alert2, amount3, loc_good1_cart, loc_alert1,
                     loc_out_of_stock_text, loc_quantity, loc_good2_price)
import HtmlTestRunner
from urllib.parse import urlparse

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_check_vehicle_accessories_modelS(self):
        driver = self.driver
        driver.get(helpers.main1)
        driver.maximize_window()
        actions = ActionChains(driver)

    # Identification of the website

        print(driver.title)
        print(driver.current_url)
        print("Check Tesla page Title")
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        print("Check Tesla page URL")

        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(driver.current_url)
            assert parsed_url.hostname == "www.tesla.com"
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Checking the transfer to the Model S module

        try:
            element1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, loc_shop)))
            actions.move_to_element(element1).perform()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_vehicle_acc1)))
            driver.find_element(By.XPATH, loc_vehicle_acc1).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on shop")

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    def test_add_good_to_cart(self):

        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        print("Added one good by default")
        time.sleep(3)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(3)

    # Checking of possibility of adding more than two goods

        driver.find_element(By.XPATH, loc_input_field).click()
        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount2)

        try:
            alert = driver.find_element(By.XPATH, loc_alert2).text
            assert alert == "Max Quantity Allowed: 2"
            print("Adding more than two goods is impossible")
        except NoSuchElementException:
            print("Can add more than two goods")
        time.sleep(3)

        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(3)

        driver.find_element(By.XPATH, loc_input_field).send_keys(amount3)
        time.sleep(3)

        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

        price1 = driver.find_element(By.XPATH, loc_good1_price).text
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(3)

        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking the price of added goods

        try:
            price = float(price1.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

    # Changing amount of goods in the cart

        driver.find_element(By.XPATH, loc_select_amount).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_select2).click()
        time.sleep(3)

    # Checking the price of added goods

        price_cart2 = driver.find_element(By.XPATH, loc_good1_price_cart).text

        try:
            price_cart3 = float(price_cart2.replace("$", ""))
            assert price_cart3 == price * 2
            print("The price is right")
        except:
            print("The price is wrong")

    # Remove goods from the cart

        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove_accept).click()
        time.sleep(3)

    # Checking if the cart is empty

        try:
            empty_cart = driver.find_element(By.XPATH, loc_empty_cart).text
            assert "Your cart is empty." == empty_cart
            print("Good deleted from cart")
        except:
            print("Good isn't deleted")

    def test_searching_field(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Search goods

        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search)))
            driver.find_element(By.XPATH, loc_search).click()
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            print("Failed to click")

    # Empty field
        time.sleep(2)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, loc_search_field)))
        driver.find_element(By.XPATH, loc_search_field).send_keys(Keys.ENTER)
        result = driver.find_element(By.XPATH, loc_search_result_empty).text
        assert result == "Please enter 2 or more characters"
        print("An empty field gets no result")
        time.sleep(2)
    # Return

        driver.back()
        time.sleep(2)

    # Searching an item

        driver.find_element(By.XPATH, loc_search).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_search_field).send_keys(name_good)
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search_result)))
        time.sleep(15)
        driver.find_element(By.XPATH, loc_search_result).click()

    # Сhecking the found product

        try:
            search_result1 = driver.find_element(By.XPATH, loc_search_result1).text
            assert search_result1 == "Model S All-Weather Interior Liners"
            print("The good is found")
        except:
            print("The good isn't found")

    def test_add_non_integer_amount(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount1)
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

    # Checking added amount of goods

        try:
            quantity = driver.find_element(By.XPATH, loc_quantity).text
            quantity = float(quantity.replace("Quantity: ", ""))
            assert quantity == 0.9
            print("Adding non integer amount of goods is possible")
        except :
            print("Adding non integer amount of goods isn't possible")

    def test_re_adding_items_to_the_cart(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()
        actions = ActionChains(driver)

        # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

        price2 = driver.find_element(By.XPATH, loc_good2_price).text
        time.sleep(3)
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(3)
        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text
        time.sleep(3)

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking price of added goods

        try:
            price = float(price2.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

        # Transfer to vehicle Model S module

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

    # Re-adding goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(2)

        try:

            alert = driver.find_element(By.XPATH, loc_alert1).text
            assert alert == "You've exceeded the maximum quantity allowed per order"
            print("Re-adding items already in the cart, the total number of which exceeds two is impossible")
        except:
            print("Re-adding is possible")

    def test_adding_out_of_stock_good(self):
        driver = self.driver
        driver.get("https://shop.tesla.com/category/vehicle-accessories/model-y")
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-y" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart
        element = driver.find_element(By.XPATH, loc_out_of_stock)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # Checking added goods in the cart

        try:
            name1 = driver.find_element(By.XPATH, loc_out_of_stock_text).text
            assert name1 == "This item is out of stock"
            print("The selected item can't be added")
        except NoSuchElementException:
            print("The good can be added")

    def tearDown(self):
        self.driver.quit()

class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_check_vehicle_accessories_modelS(self):
        driver = self.driver
        driver.get(helpers.main1)
        driver.maximize_window()
        actions = ActionChains(driver)

    # Identification of the website

        print(driver.title)
        print(driver.current_url)
        print("Check Tesla page Title")
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        print("Check Tesla page URL")

        try:
            parsed_url = urlparse(driver.current_url)
            assert parsed_url.hostname == "www.tesla.com"
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Checking the transfer to the Model S module

        try:
            element1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, loc_shop)))
            actions.move_to_element(element1).perform()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_vehicle_acc1)))
            driver.find_element(By.XPATH, loc_vehicle_acc1).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on shop")

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    def test_add_good_to_cart(self):

        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        print("Added one good by default")
        time.sleep(2)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(2)

    # Checking of possibility of adding more than two goods

        driver.find_element(By.XPATH, loc_input_field).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount2)

        try:
            alert = driver.find_element(By.XPATH, loc_alert2).text
            assert alert == "Max Quantity Allowed: 2"
            print("Adding more than two goods is impossible")
        except NoSuchElementException:
            print("Can add more than two goods")
        time.sleep(2)

        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)

        driver.find_element(By.XPATH, loc_input_field).send_keys(amount3)
        time.sleep(2)

        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)

        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(2)

        price1 = driver.find_element(By.XPATH, loc_good1_price).text
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(2)

        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking the price of added goods

        try:
            price = float(price1.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

    # Changing amount of goods in the cart

        driver.find_element(By.XPATH, loc_select_amount).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_select2).click()
        time.sleep(3)

    # Checking the price of added goods

        price_cart2 = driver.find_element(By.XPATH, loc_good1_price_cart).text

        try:
            price_cart3 = float(price_cart2.replace("$", ""))
            assert price_cart3 == price * 2
            print("The price is right")
        except:
            print("The price is wrong")

    # Remove goods from the cart

        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove_accept).click()
        time.sleep(3)

    # Checking if the cart is empty

        try:
            empty_cart = driver.find_element(By.XPATH, loc_empty_cart).text
            assert "Your cart is empty." == empty_cart
            print("Good deleted from cart")
        except:
            print("Good isn't deleted")

    def test_searching_field(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Search goods

        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search)))
            driver.find_element(By.XPATH, loc_search).click()
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            print("Failed to click")

    # Empty field
        time.sleep(2)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, loc_search_field)))
        driver.find_element(By.XPATH, loc_search_field).send_keys(Keys.ENTER)
        time.sleep(3)
        result = driver.find_element(By.XPATH, loc_search_result_empty).text
        assert result == "Please enter 2 or more characters"
        print("An empty field gets no result")
        time.sleep(2)
    # Return

        driver.back()
        time.sleep(2)

    # Searching an item

        driver.find_element(By.XPATH, loc_search).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_search_field).send_keys(name_good)
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search_result)))
        time.sleep(15)
        driver.find_element(By.XPATH, loc_search_result).click()

    # Сhecking the found product

        try:
            search_result1 = driver.find_element(By.XPATH, loc_search_result1).text
            assert search_result1 == "Model S All-Weather Interior Liners"
            print("The good is found")
        except:
            print("The good isn't found")

    def test_add_non_integer_amount(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount1)
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

    # Checking added amount of goods

        try:
            quantity = driver.find_element(By.XPATH, loc_quantity).text
            quantity = float(quantity.replace("Quantity: ", ""))
            assert quantity == 0.9
            print("Adding non integer amount of goods is possible")
        except :
            print("Adding non integer amount of goods isn't possible")

    def test_re_adding_items_to_the_cart(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()
        actions = ActionChains(driver)

        # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

        price2 = driver.find_element(By.XPATH, loc_good2_price).text
        time.sleep(3)
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(3)
        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text
        time.sleep(3)

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking price of added goods

        try:
            price = float(price2.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

        # Transfer to vehicle Model S module

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

    # Re-adding goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(2)

        try:

            alert = driver.find_element(By.XPATH, loc_alert1).text
            assert alert == "You've exceeded the maximum quantity allowed per order"
            print("Re-adding items already in the cart, the total number of which exceeds two is impossible")
        except:
            print("Re-adding is possible")

    def test_adding_out_of_stock_good(self):
        driver = self.driver
        driver.get("https://shop.tesla.com/category/vehicle-accessories/model-y")
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-y" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart
        element = driver.find_element(By.XPATH, loc_out_of_stock)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # Checking added goods in the cart

        try:
            name1 = driver.find_element(By.XPATH, loc_out_of_stock_text).text
            assert name1 == "This item is out of stock"
            print("The selected item can't be added")
        except NoSuchElementException:
            print("The good can be added")

    def tearDown(self):
        self.driver.quit()

class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_check_vehicle_accessories_modelS(self):
        driver = self.driver
        driver.get(helpers.main1)
        driver.maximize_window()
        actions = ActionChains(driver)

    # Identification of the website

        print(driver.title)
        print(driver.current_url)
        print("Check Tesla page Title")
        try:
            assert "Electric Cars, Solar & Clean Energy | Tesla" in driver.title
            print("Test result: Page title is OK: ", driver.title)
        except AssertionError:
            print("Test result: Page title is different", driver.title)

        print("Check Tesla page URL")

        try:
            parsed_url = urllib.parse.urlparse(driver.current_url)
            assert parsed_url.hostname == "www.tesla.com"
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Checking the transfer to the Model S module

        try:
            element1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, loc_shop)))
            actions.move_to_element(element1).perform()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_vehicle_acc1)))
            driver.find_element(By.XPATH, loc_vehicle_acc1).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on shop")

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

        try:
            parsed_url = urllib.parse.urlparse(driver.current_url)
            assert parsed_url.hostname == "shop.tesla.com" and parsed_url.path == "/category/vehicle-accessories/model-s"
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    def test_add_good_to_cart(self):

        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        print("Added one good by default")
        time.sleep(3)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(3)

    # Checking of possibility of adding more than two goods

        driver.find_element(By.XPATH, loc_input_field).click()
        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount2)

        try:
            alert = driver.find_element(By.XPATH, loc_alert2).text
            assert alert == "Max Quantity Allowed: 2"
            print("Adding more than two goods is impossible")
        except NoSuchElementException:
            print("Can add more than two goods")
        time.sleep(3)

        driver.find_element(By.XPATH, loc_input_field).clear()
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(3)

        driver.find_element(By.XPATH, loc_input_field).send_keys(amount3)
        time.sleep(3)

        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

        price1 = driver.find_element(By.XPATH, loc_good1_price).text
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(3)

        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking the price of added goods

        try:
            price = float(price1.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

    # Changing amount of goods in the cart

        driver.find_element(By.XPATH, loc_select_amount).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_select2).click()
        time.sleep(3)

    # Checking the price of added goods

        price_cart2 = driver.find_element(By.XPATH, loc_good1_price_cart).text

        try:
            price_cart3 = float(price_cart2.replace("$", ""))
            assert price_cart3 == price * 2
            print("The price is right")
        except:
            print("The price is wrong")

    # Remove goods from the cart

        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove).click()
        time.sleep(3)
        driver.find_element(By.XPATH, loc_remove_accept).click()
        time.sleep(3)

    # Checking if the cart is empty

        try:
            empty_cart = driver.find_element(By.XPATH, loc_empty_cart).text
            assert "Your cart is empty." == empty_cart
            print("Good deleted from cart")
        except:
            print("Good isn't deleted")

    def test_searching_field(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Search goods

        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search)))
            driver.find_element(By.XPATH, loc_search).click()
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            print("Failed to click")

    # Empty field
        time.sleep(2)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, loc_search_field)))
        driver.find_element(By.XPATH, loc_search_field).send_keys(Keys.ENTER)
        result = driver.find_element(By.XPATH, loc_search_result_empty).text
        assert result == "Please enter 2 or more characters"
        print("An empty field gets no result")
        time.sleep(2)
    # Return

        driver.back()
        time.sleep(2)

    # Searching an item

        driver.find_element(By.XPATH, loc_search).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_search_field).send_keys(name_good)
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_search_result)))
        time.sleep(15)
        driver.find_element(By.XPATH, loc_search_result).click()

    # Сhecking the found product

        try:
            search_result1 = driver.find_element(By.XPATH, loc_search_result1).text
            assert search_result1 == "Model S All-Weather Interior Liners"
            print("The good is found")
        except:
            print("The good isn't found")

    def test_add_non_integer_amount(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()

    # Checking the right page

        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

    # Adding a good to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).clear()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_input_field).send_keys(amount1)
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(3)

    # Checking added amount of goods

        try:
            quantity = driver.find_element(By.XPATH, loc_quantity).text
            quantity = float(quantity.replace("Quantity: ", ""))
            assert quantity == 0.9
            print("Adding non integer amount of goods is possible")
        except :
            print("Adding non integer amount of goods isn't possible")

    def test_re_adding_items_to_the_cart(self):
        driver = self.driver
        driver.get(helpers.main2)
        driver.maximize_window()
        actions = ActionChains(driver)

        # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-s" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_plus_quantity).click()
        print("Added two goods")
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(4)

        price2 = driver.find_element(By.XPATH, loc_good2_price).text
        time.sleep(3)
        driver.find_element(By. XPATH, loc_view_cart).click()
        time.sleep(3)
        price_cart = driver.find_element(By.XPATH, loc_good1_price_cart).text
        time.sleep(3)

    # Checking added goods in the cart

        try:
            name = driver.find_element(By.XPATH, loc_good1_cart).text
            assert name == "Model S All-Weather Interior Liners"
            print("The selected Good is added")
        except NoSuchElementException:
            print("The good isn't added")

    # Checking price of added goods

        try:
            price = float(price2.replace("$", ""))
            price_cart = float(price_cart.replace("$", ""))
            assert price == price_cart
            print("The price is right")
        except:
            print("The price is wrong")
        time.sleep(3)

        # Transfer to vehicle Model S module

        try:
            element2 = driver.find_element(By.XPATH, loc_vehicle_acc2)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of(element2))
            actions.move_to_element(element2).perform()
            hover_script = """
                    var event = new MouseEvent('mouseover', {bubbles: true, cancelable: true, view: window});
                    arguments[0].dispatchEvent(event);
                    """
            driver.execute_script(hover_script, element2)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, loc_modelS)))
            driver.find_element(By.XPATH, loc_modelS).click()
        except (NoSuchElementException, TimeoutException):
            print("Failed to click on Vehicle Accessories")

    # Re-adding goods to the cart

        driver.find_element(By.XPATH, loc_good1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, loc_add_cart).click()
        time.sleep(2)

        try:

            alert = driver.find_element(By.XPATH, loc_alert1).text
            assert alert == "You've exceeded the maximum quantity allowed per order"
            print("Re-adding items already in the cart, the total number of which exceeds two is impossible")
        except:
            print("Re-adding is possible")

    def test_adding_out_of_stock_good(self):
        driver = self.driver
        driver.get("https://shop.tesla.com/category/vehicle-accessories/model-y")
        driver.maximize_window()

    # Checking the right page
        try:
            assert "https://shop.tesla.com/category/vehicle-accessories/model-y" in driver.current_url
            print("Test result: Page URL is OK: ", driver.current_url)
        except AssertionError:
            print("Test result: Page URL is different", driver.current_url)

        # Adding a goods to the cart
        element = driver.find_element(By.XPATH, loc_out_of_stock)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # Checking added goods in the cart

        try:
            name1 = driver.find_element(By.XPATH, loc_out_of_stock_text).text
            assert name1 == "This item is out of stock"
            print("The selected item can't be added")
        except NoSuchElementException:
            print("The good can be added")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

if __name__ == "__main__":
    unittest.main(AllureReports)
