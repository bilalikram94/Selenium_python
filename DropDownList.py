from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
class DropDownList:

    def DropDown(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.get(baseURL)
        driver.implicitly_wait(10)
        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz By Value")
        time.sleep(2)

        sel.select_by_index('2')
        print("select Honda by Index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW with Visible Text")
        time.sleep(2)

        sel.select_by_index(2)
        print("select Honda by Index")




ff = DropDownList()
ff.DropDown()