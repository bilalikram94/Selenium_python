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
        FindElementByClass = driver.find_element_by_class_name("displayed-class")
        FindElementByClass.send_keys("element found")
        if FindElementByClass is not None:
            print("element found")

        elementByTag = driver.find_element_by_tag_name('h1')
        text = elementByTag.text
        if elementByTag is not None:
            print("element found by tag and the text on the element is: " + text)



ff = FindByClassTag()
ff.test()


