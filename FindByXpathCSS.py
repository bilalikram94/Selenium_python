from selenium import webdriver


class FindByXpathCSS:
    def test (self):

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("we found an element by XPATH")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("we found an element by CSS")
        driver.quit()


ff = FindByXpathCSS()
ff.test()
