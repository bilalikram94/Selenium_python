"""
Dependencies UsingWrappers.py
"""
from selenium.webdriver.common.by import By

class HandyWrappers():
    def __init__(self, driver):
        self.driver = driver

    def getByType (self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link text":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css selector":
            return By.CSS_SELECTOR
        elif locatorType == "partial link text":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator is invalid")
        return False
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("element is found")
        except:
            print("Element not found")
        return element


