# Main links
main1 = "https://www.tesla.com/"
main2 = "https://shop.tesla.com/category/vehicle-accessories/model-s"

# Locators
loc_shop = "//span[@class='tds-site-nav-item-text'][contains(.,'Shop')]"
loc_vehicle_acc1 = "//h3[contains(.,'Vehicle Accessories')]"
loc_vehicle_acc2 = "//*[@id='main-menu']/div[1]/ol/li[2]/div"
loc_modelS = "(//a[contains(.,'Model S')])[1]"
loc_good1 = "(//a[contains(.,'Model S All-Weather Interior Liners')])[1]"
loc_good1_cart = "//p[contains(.,'Model S All-Weather Interior Liners')]"
loc_good1_price = "//p[contains(.,'$250.00')]"
loc_good2_price = "//span[contains(.,'$500.00')]"
loc_good1_price_cart = "(//h2[@class='tds-text--h4'])[3]"
loc_plus_quantity = "(//button[contains(.,'+')])[1]"
loc_minus_quantity = "(//button[contains(.,'-')])[1]"
loc_quantity = "//span[contains(.,'Quantity: 2')]"
loc_input_field = "(//input[@class='tds-form-input-text'])[1]"
loc_add_cart = "//input[@id='addToCartBtn']"
loc_view_cart = "//button[@class='tds-btn tds-btn--secondary']"
loc_remove = "//a[contains(.,'Remove')]"
loc_remove_accept = "//button[contains(.,'Yes, Remove')]"
loc_select_amount = "//button[@class = 'tds-dropdown-trigger']"
loc_select2 = "//span[contains(.,'2')]"
loc_empty_cart = "//p[contains(@class,'empty-cart-message')]"
loc_search = "//div[@class='tds-form-input tds-form-input--default tds-form-input--collapsed']"
loc_search_field = "//input[@id='1']"
loc_search_result = "//li[@class='search-suggestion']"
loc_search_result1 = "//a[contains(.,'Model S All-Weather Interior Liners')]"
loc_search_result_empty = "//span[contains(.,'Please enter 2 or more characters')]"
loc_out_of_stock = "(//a[contains(.,'Model Y Air Mattress')])[1]"
loc_out_of_stock_text = "(//div[contains(.,'This item is out of stock')])[9]"
loc_alert1 = "(//p[@class='alert-text message'])[1]"
loc_alert2 = "//span[contains(.,'Max Quantity Allowed: 2')]"


# variables
name_good = "Model S All-Weather"
amount1 = 0.9
amount2 = 3
amount3 = 1
