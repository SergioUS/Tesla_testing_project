import random
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service


#link tesla
tsl = "https://www.tesla.com/"

# Locators for maim page
hea_der = "//header/h1[1]/a[1]/*[1]"
char_ng = "//span[contains(.,'Charging')]"
enr_g = "(//span[contains(.,'Energy')])[1]"
shop = "(//span[contains(.,'Shop')])[1]"

#Button lifestyle
Btn_lfs = "(//a[@href='/category/lifestyle'])[1]"

#Locators for lifestyle page
Bst_sel = "lifestyle.best-sellers"
Pg_Cat = "page--category"
Bgs = "lifestyle.bags"
Mn_log = "left-menu__logo"

#page scroll
Srl = "window.scrollTo(0,6000)"

#locators of product
pic = "(//img[@alt='Wireless Portable Charger'])[1]"
txt = "(//a[contains(.,'Wireless Portable Charger')])[1]"

#Locators of product's page
prd_ttl = "(//h2[contains(.,'Wireless Portable Charger')])[1]"
ing_prd = "(//img[@alt='Wireless Portable Charger'])[1]"
prd_dcr = "(//div[contains(@class,'content')])[33]"
prd_qu_fld = "(//div[@class='quantity-picker-container'])[1]"
prd_cred_pr = "(//div[contains(@class,'credit-promotion-message')])[1]"
Lo_mnCh = "//h1[@id='left-menu__logo']"

#Locators for pink charger
pink = "//input[@data-colorname='Rose Gold']"
quan_pnk = "(//button[contains(.,'+')])[2]"
Add_to_ct = "(//input[@id='addToCartBtn'])[2]"
Check_OT = "//button[contains(.,'Checkout')]"


#Locator for quantity field neg test
qua_field = "//input[@id='4']"

#Locators for white charger
white = "//input[@data-colorname='White']"
quan_white = "//input[@id='5']"
Add_to_White = "(//input[@id='addToCartBtn'])[3]"

#Locators for charger/no colors chosen
qun_field = "//input[@id='3']"
Add_to_ctNCR = "(//input[@data-item-added='Added'])[1]"

#Locators for black color/0 input
black = "//input[@data-colorname='Black']"
quan_black = "//input[@id='3']"
Add_to_Black = "(//input[@id='addToCartBtn'])[1]"

