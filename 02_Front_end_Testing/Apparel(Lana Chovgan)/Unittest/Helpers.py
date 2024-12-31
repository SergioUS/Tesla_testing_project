from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

Shop = "//a[@id='dx-nav-item--shop']"
Apparel_1 = "//img[@alt='Apparel']"
Apparel_2 = "//a[contains(text(),'Apparel')]"
Onesies = "//a[@href='/category/apparel/kids#kids.onesies']"
Onesie = "//img[@alt='Endless Energy Onesie']"
Hat = "(//img[@alt='Cyberbeast Trucker Hat'])[1]"
Hats = "//a[@href='/category/apparel/men#men.hats']"
SizeOnesies = "//input[@id='2031682-00-ANB']"

def hover_shop(driver):
    element_to_hover = driver.find_element(By.XPATH, "//a[@id='dx-nav-item--shop']")
# Create an ActionChains object
    actions = ActionChains(driver)
# Perform the hover action
    actions.move_to_element(element_to_hover).perform()