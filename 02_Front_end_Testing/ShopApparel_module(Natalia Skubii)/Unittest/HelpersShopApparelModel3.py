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
shop_link = "(//span[contains(.,'Shop')])[1]"


#Apparel link
apparel_link = "//a[contains(.,'Apparel')]"

#Kids-Onesie link

onesie = "//a[contains(.,'Onesies')]"

#Men-Tees link

tees = "(//a[contains(.,'Tees')])[1]"

#Built for Any Planet Trucker Hat link
hat_link = "(//img[contains(@alt,'Built for Any Planet Trucker Hat')])[1]"

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

#


#Men's Cybertruck Cityscape Tee link
partial_link = "//a[@data-productsku='2024512-00-A']"

#Sizes buttons:
size_S = "//input[@id='2024512-00-AS']"
size_M = "(//input[@value='M'])[1]"
size_L = "//input[@aria-checked='true']"
size_XL = "//input[@id='2024515-00-AXL']"
size_XXL = "(//label[contains(.,'XXL')])[1]"
size_3XL = "//input[@id='2024517-00-A3XL']"

#Quantity line
quantity_input = "(//input[@type='number'])[1]"

#Add to Cart button
add_to_cart = "//input[@id='addToCartBtn']"

#Page Cart
page_cart = "//section[@class='tds-modal-content']"

#Vehicles link
vehicles_link = "//span[contains(.,'Vehicles')]"

#Order button
order_button = "(//a[contains(.,'Order')])[2]"

page_order = "//h1[contains(.,'Tesla homepageSkip to main content')]"
right_carousel = "//*[@id='main-content']/section/div[1]/div/button[2]"

left_carousel = "//button[contains(@class,'next')]"

scribble_onesie = "(//a[contains(.,'Scribble T Logo Onesie')])[1]"



#Gray color button
gray_color = "//input[@data-colorname='Gray']"
white_color = "//input[@data-colorname='White']"

#Sizes button in the "Scribble T logo onesie"
size_6 = "//input[@id='8529383-00-A6']"
size_12 = "(//input[@value='12'])[1]"
size_18 = "//input[@id='8529390-00-A18']"
size_24 = "//input[contains(@id,'8529391-00-A24')]"

#Quantity in the "Scribble T logo onesie"
quantity_input1 = "//input[@id='4']"

#Add to Cart button in the "Scribble T logo onesie"
add_to_cart1 = "(//input[@value='Add to Cart'])[2]"

page_cart1 = "(//div[@class='tds-modal-header'])[1]"

#Learn link Model3
learn = "(//a[contains(.,'Learn')])[3]"

#Learn More button
learn_more = "(//a[contains(.,'Learn More')])[2]"

#Experience Model 3 button
experience = "//a[@title='Experience Model 3'][contains(.,'Experience Model 3')]"

#Schedule button
schedule = "//button[contains(.,'Schedule')]"

#First name input
first_name = "//input[@name='firstName']"

# Last name input
last_name = "//input[@name='lastName']"

#Email address input
email_address = "//input[@name='email']"

#Phone number input
phone = "//input[@name='phone']"

# Submit button
submit = "//button[contains(.,'Submit')]"

#Error message "Requared input field" in line First name
error_message1 = "//div[contains(text(),'Required input field')]"

#Error message "Please enter a phone number" in the line "Phone number"
error_message2 = "//div[contains(text(),'Please enter a phone number')]"

#Order link
order = "(//a[contains(.,'Order')])[2]"

#Lease button
lease = "//button[@label='Lease']"

#Order now button in Lease menu
order_lease = "//button[contains(.,'Order Now')]"

#Order with card buton
order_card = "//button[contains(.,'Order with Card')]"

#Input First name in Account Details
first_name_account = "//input[@id='FIRST_NAME']"

#Input Last Name in Account Details
last_name_account = "//input[@id='LAST_NAME']"

#Input Email address in Account Details
email_account = "//input[@id='EMAIL']"

#Input Confirm email address in Account Details
confirm_account = "//input[@id='EMAIL_CONFIRM']"

#Error message in Account Details
error_message3 = "//div[@class='tds-form-feedback-text']"

#Error message
error_message4 = "//div[contains(text(),'Required input field')]"



