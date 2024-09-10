#Helper for Unittest-ShopApparel-Model3
#Natalia Skubii

from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By


def delay():
    time.sleep(random.randint(1, 3))




# Tesla URL
tesla_url ="https://www.tesla.com/"

#Shop Link
shop_link = "//span[@class='tds-site-nav-item-text'][contains(.,'Shop')]"


#Apparel link
apparel_link = "//a[contains(.,'Apparel')]"

#Apparel url
apparel_url = "https://shop.tesla.com/category/apparel"


#Built for Any Planet Trucker Hat link
hat_link = "(//img[contains(@alt,'Built for Any Planet Trucker Hat')])[1]"

#Men Tees url

menTees_url = "https://shop.tesla.com/category/apparel/men#men.tees"
#Email me when this item is restocked link
emailRestoked_link = "(//a[contains(.,'Email me when this item is restocked')])[1]"

#Enter email address
input_email_link = "(//input[@aria-label='Enter email address'])[1]"

#Notify me button:
notify_button = "(//input[@value='Notify Me'])[1]"

#Error message
invalid_email_error = "//div[contains(text(),'Please enter a valid email address')]"

def moving_to_new_window(driver):
    first_window = driver.window_handles[0]
    all_windows = driver.window_handles
    for window in all_windows:
        if window != first_window:
            new_window = window
            driver.switch_to.window(first_window)
            driver.switch_to.window(new_window)

#Scroll down the page
def moving_to_new_window1(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

#Men's Cybertruck Cityscape Tee link
partial_link = "(//img[contains(@data-productsku,'2024512-00-A')])[1]"

#Sizes buttons:
size_S = "//input[@id='2024512-00-AS']"
size_M = "//input[@id='2024513-00-AM']"
size_L = "//input[@id='2024514-00-AL']"
size_XL = "//input[@id='2024515-00-AXL']"
size_XXL = "(//label[contains(.,'XXL')])[1]"
size_3XL = "//input[@id='2024517-00-A3XL']"

#Quantity line
quantity_input = "(//input[@type='number'])[1]"

#Add to Cart button
add_to_cart = "//input[@id='addToCartBtn']"