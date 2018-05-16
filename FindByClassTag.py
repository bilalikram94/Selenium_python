from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.webdriver import WebDriver

baseURL = "https://learn.letskodeit.com/p/practice"
driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
#binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
#driver = webdriver.Firefox(firefox_binary=binary)

class FindByClassTag:
    @staticmethod
    def test():
        driver.get(baseURL)
        FindElementByXpath = driver.find_elements_by_xpath("//input[@id='displayed-text']")
        FindElementByXpath
        if FindElementByClass is not None:
            print("element found")


ff = FindByClassTag()
ff.test()


