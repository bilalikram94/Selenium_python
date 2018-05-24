from selenium import webdriver
from wrappers.HandyWrappers import HandyWrappers
from selenium.webdriver.common.by import By
import time


class ElementPresentCheck:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(
            "C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        elementResult = hw.isElementPresent("name", By.ID)
        print(str(elementResult))

        elementResult1 = hw.elementPresenceCheck("//input[@id = 'name1']", byType="xpath")
        print(str(elementResult1))


ff = ElementPresentCheck()
ff.test()
