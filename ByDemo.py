from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo:
    def test(self):
        driver = webdriver.Chrome('C:\\Users\\Bilal.Ikram\\PycharmProjects'
                                  '\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe')
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.get(baseUrl)
        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print("we found an element by ID")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("we found an element by Xpath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")
        if elementByLinkText is not None:
            print("we found an element by Link Text")

ff = ByDemo()
ff.test()
