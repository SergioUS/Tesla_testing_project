# Helpers for DmitryA_ShopVehicleAccessoriesModelX_unittest.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests


def delay1_5():
    time.sleep(random.randint(1,5))

# ------------------------------Helpers for Vehicle Accessories Tesla Model X site-------------------------------

# Tesla URL
tesla_url ="https://www.tesla.com/"

# Homepage API check
def check_api(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("----API check: Url has ", requests.get(driver.current_url).status_code, " as Status Code")
        print("----API response code is OK")
    else:
        print("ATTENTION! API response code is not 200", "Current code is:", code)

#Shop Link
shop_link = "//header/ol[1]/li[5]/a[1]/span[1]"


#Vehicle Accessories link
VehicleAccessories_link = "//a[contains(text(),'Vehicle Accessories')]"

#Vehicle Accessories link2
VehicleAccessories_link2 = '//*[@id="main-menu"]/div[1]/ol/li[2]/div'

#Vehicle Accessories url
VehicleAccessories_url = "https://shop.tesla.com/category/vehicle-accessories"

#Vehicle Accessories Model X link
VehicleAccessoriesModelX_link = '//*[@id="tile-1"]/div/div[1]/div/div[4]/p/a'

#Vehicle Accessories Model X url
VehicleAccessoriesModelX_url = "https://shop.tesla.com/category/vehicle-accessories/model-x"

#Vehicle Accessories Model X Pet Liner link
PetLiner_link = '//*[@id="category--model_x--mx_interior"]/ul/li[1]/div[2]/div/div[1]/a'

#Vehicle Accessories Model X Pet Liner url
PetLiner_url = "https://shop.tesla.com/product/model-x-pet-liner"

#Vehicle Accessories Model X Key Fob link
KeyFob_link = "//a[contains(text(),'Model X Key Fob')]"

#Vehicle Accessories/Model-X/Key Fob url
KeyFob_url = "https://shop.tesla.com/product/model-x-key-fob"

#Vehicle Accessories Model X Car Cover link
CarCover_link = "//a[contains(text(),'Model X Car Cover')]"

#Vehicle Accessories/Model-X/Car Cover url
CarCover_url = "https://shop.tesla.com/product/model-x-car-cover"

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

#Quantity line
quantity_input = "//input[@id='3']"

#Add to Cart and Page cart
add_to_cart = "//input[@id='addToCartBtn']"
page_cart = "//body/main[@id='content-main']/div[1]/div[1]/div[2]/div[1]"




