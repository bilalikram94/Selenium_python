from selenium import webdriver
from selenium.webdriver.common.by import By

baseURL = "https://learn.letskodeit.com/p/practice"
driver = webdriver.Chrome(
    "C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\\chromedriver.exe")


class ListOfElements:
    def test(self):
        driver.get(baseURL)
        elementListByClass = driver.find_elements_by_class_name("inputs")
        length = len(elementListByClass)
        if elementListByClass is not None:
            print("size of the list is:" + str(length))

        elementListBytag = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListBytag)
        if elementListBytag is not None:
            print("TagName-->size of the list is:" + str(length2))


ff = ListOfElements()
ff.test()
