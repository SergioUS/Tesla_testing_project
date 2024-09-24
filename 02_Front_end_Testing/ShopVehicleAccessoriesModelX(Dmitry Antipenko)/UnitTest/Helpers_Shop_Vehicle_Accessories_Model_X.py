# Helpers for DmitryA_ShopVehicleAccessoriesModelX_unittest.py
from pycparser.c_ast import Continue
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

# Shop Link
shop_link = "//header/ol[1]/li[5]/a[1]/span[1]"


# Vehicle Accessories link
VehicleAccessories_link = "//a[contains(text(),'Vehicle Accessories')]"

# Vehicle Accessories link2
VehicleAccessories_link2 = '//*[@id="main-menu"]/div[1]/ol/li[2]/div'

# Vehicle link
Vehicle_link = "//span[contains(.,'Vehicles')]"

# Vehicle Accessories url
VehicleAccessories_url = "https://shop.tesla.com/category/vehicle-accessories"

# Vehicle Accessories Model X link
VehicleAccessoriesModelX_link = '//*[@id="tile-1"]/div/div[1]/div/div[4]/p/a'

# Vehicle Accessories Model X url
VehicleAccessoriesModelX_url = "https://shop.tesla.com/category/vehicle-accessories/model-x"

# Vehicle Accessories Model X Pet Liner link
PetLiner_link = '//*[@id="category--model_x--mx_interior"]/ul/li[1]/div[2]/div/div[1]/a'

# Vehicle Accessories Model X Pet Liner url
PetLiner_url = "https://shop.tesla.com/product/model-x-pet-liner"

# Vehicle Accessories Model X Car Cover link
CarCover_link = "//a[contains(text(),'Model X Car Cover')]"

# Vehicle Accessories/Model-X/Car Cover url
CarCover_url = "https://shop.tesla.com/product/model-x-car-cover"

# Vehicle Accessories Model X Key Fob link
KeyFob_link = "//a[contains(text(),'Model X Key Fob')]"

# Vehicle Accessories/Model-X/Key Fob url
KeyFob_url = "https://shop.tesla.com/product/model-x-key-fob"

# Vehicle Accessories Model X Mud Flaps link
MudFlaps_link = "//a[contains(.,'Model X Mud Flaps')]"

# Vehicle Accessories Model X Mud Flaps Price link
MudFlapsPrice_link = '//*[@id="productInfo"]/div[1]/div[2]/div/div[2]/div[1]/div/div/p'

# Vehicle Accessories/Model-X/Mud Flaps url
MudFlaps_url = "https://shop.tesla.com/product/model-x-mud-flaps"

# Vehicle Vehicle Model X link
VehicleModelX_link = "//img[@alt='Model X']"

# Vehicle Model X Demo Drive link
Demo_Drive_X_link = "(//span[contains(.,'Demo Drive')])[1]"

# Demo Drive Model X Schedule link
Demo_Drive_X_Schedule_link = "//button[contains(.,'Schedule')]"

# Vehicle Module X Demo Drive url
Demo_Drive_X_url = "https://www.tesla.com/drive?selectedModel=modelx"

# First name, Last name, Email and Phone number for registration form
FN_link = "(//input[contains(@class,'tds-form-input-text')])[2]"
LN_link = "(//input[contains(@class,'tds-form-input-text')])[3]"
Email_link = "//input[contains(@name,'email')]"
PN_link = "//input[contains(@name,'phone')]"
Submit = "//button[contains(.,'Submit')]"

# Vehicle Accessories/Model-X/Mud Flaps/Checkout link
Checkout = "//button[contains(.,'Checkout')]"

# Email2 link
Email2 = "//input[contains(@id,'email')]"

# Button Continue link
Continue2 = "//button[contains(.,'Continue')]"

def moving_to_new_window(driver):
    first_window = driver.window_handles[0]
    all_windows = driver.window_handles
    for window in all_windows:
        if window != first_window:
            new_window = window
            driver.switch_to.window(first_window)
            driver.switch_to.window(new_window)

# Scroll down the page
def moving_to_new_window1(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

# Quantity line
quantity_input = "//input[@id='3']"

# Add to Cart and Page cart
add_to_cart = "//input[@id='addToCartBtn']"
page_cart = "//body/main[@id='content-main']/div[1]/div[1]/div[2]/div[1]"

# Search Line for Model X link
S_l_ModelX_link = "//input[contains(@id,'1')]"
page_s_l_model_x = "//input[contains(@id,'1')]"



