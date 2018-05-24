from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText:
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("text on element is:" + elementText)
        time.sleep(2)
        driver.quit()
ff = GetText()
ff.test()