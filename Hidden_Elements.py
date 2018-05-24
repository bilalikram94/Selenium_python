from selenium import webdriver
import time
class HiddenElements:
    def Elements(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        # Find the state of the Text box
        textboxElement = driver.find_element_by_id("displayed-text")
        textboxState = textboxElement.is_displayed() # True if visible , False if not hidden
        # Exception oif not present in DOM
        print("Text is visible" + str(textboxState))
        time.sleep(2)

        #click the Hide Button
        driver.find_element_by_id("hide-textbox").click()
        time.sleep(2)
        #Find the state of the text box
        textboxState = textboxElement.is_displayed()
        print("Text is visible" + str(textboxState))
        time.sleep(2)
        #Click the show button
        driver.find_element_by_id("show-textbox").click()
        time.sleep(2)
        #find the state of the text box
        textboxState = textboxElement.is_displayed()
        print("Text is visible" + str(textboxState))
        time.sleep(2)
        #Close Browser
        driver.quit()


ff = HiddenElements()
ff.Elements()