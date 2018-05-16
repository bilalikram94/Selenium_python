from selenium import webdriver
import  time
from selenium.webdriver.common.keys import Keys

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
 	
	FindElementByName = driver.find_element_by_name("to")
        FindElementByName.click()
        FindElementByName.send_keys("Recipient Email")
        if FindElementByName is not None:
            print("Sender email added")

        
        FindElementByClassName = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
        FindElementByClassName.click()
        FindElementByClassName.send_keys("Type Message to recipient")
        FindElementByClassName.send_keys(Keys.CONTROL+Keys.ENTER)
        if FindElementByClassName is not None:
            print("Message Typed")
            print("Mission Complete")

       # FindElementByClassName1 = driver.find_element_by_css_selector("T-I J-J5-Ji aoO T-I-atl L3").send_keys(Keys.CONTROL+Keys.ENTER)
       # if FindElementByClassName1 is not None:
        #    print("Mission Complete")
       # time.sleep(3)


ff = Login()
ff.test()
