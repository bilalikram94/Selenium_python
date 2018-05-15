from selenium import webdriver
import time


class searchById ():
    # noinspection PyUnreachableCode
    @staticmethod
    def test():

        baseURL = "https://www.google.com"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium"
                                  "\\webdriver\\chromedriver.exe")
        driver.get(baseURL)
        FindElementById = driver.find_element_by_id("lst-ib")

        if FindElementById is not None:
            print("Element found by ID")

        clickElement = driver.find_element_by_id("lst-ib")
        clickElement.click()
        if clickElement is not None:
            print("button clicked")

        search = driver.find_element_by_id("lst-ib")
        search.send_keys("horse")

        if search is not None:
            print("keys sent")

        return search.send_keys()
        FindByLinkText = driver.find_element_by_link_text("Horse")
        if FindByLinkText is not None:
            print("element found by link text")
        time.sleep(20)


ff = searchById()
ff.test()
