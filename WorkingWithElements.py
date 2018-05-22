from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElements:
    def testListOfElements(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome('C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe')
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        radioBtn = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioBtn)
        print("Size of the List:" + str(size))
        for radioButton in radioBtn:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(3)


ff = WorkingWithElements()
ff.testListOfElements()