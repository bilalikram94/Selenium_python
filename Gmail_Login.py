from selenium import webdriver
import  time

class Login:
    @staticmethod
    def test():
        baseURL = "https://www.google.com/gmail/about/"
        driver = webdriver.Firefox()

        driver.get(baseURL)
        #driver.fullscreen_window()
        FindElementByLinkText = driver.find_element_by_link_text("SIGN IN")
        if FindElementByLinkText is not None:
            print("element found by link text")

        FindElementByLinkText.click()

        FindElementByXpath = driver.find_element_by_xpath("//input[@id='identifierId']")
        FindElementByXpath.click()
        if FindElementByXpath is not None:
            print("element found by XPATH")
        FindElementByXpath.send_keys("#Enter Your Email")

        FindElementByCSS = driver.find_element_by_xpath("//div[@id='identifierNext']")
        FindElementByCSS.click()
        if FindElementByCSS is not None:
            print("Element found by Xpath")
        time.sleep(3)
        FindElementByXpath1 = driver.find_element_by_xpath("//input[@name='password']")
        FindElementByXpath1.send_keys("#enter password")
        if FindElementByXpath1 is not None:
            print("Password entered through Xpath")

        FindElementByXpath2 = driver.find_element_by_xpath("//div[@id='passwordNext']")
        FindElementByXpath2.click()
        if FindElementByXpath2 is not None:
            print("Login Successful")

        time.sleep(5)


ff = Login()
ff.test()
