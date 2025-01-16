
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

# Main links
main = "https://www.tesla.com/"
mytestpage1 = "https://www.tesla.com/we-robot"

# Function

def assert_subtitles(name, element):
    try:
        assert name in element.text
        print("'" + name + "'" + " was found")
    except Exception as e:
        print("'" + name + "'" + " was Not found")

# Locators



