"""
Need to import/download Handywrappers for the code to run other wise it will fail
Dependencies HandyWrappers
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wrappers.HandyWrappers import HandyWrappers

class UsingWrappers:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textfield = hw.getElement("name")
        textfield.send_keys("testing")
        time.sleep(2)
        textfield2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textfield2.clear()



        time.sleep(2)
        driver.quit()
ff = UsingWrappers()
ff.test()