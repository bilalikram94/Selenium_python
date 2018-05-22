from selenium import webdriver
import time


class RadioButtonandCheckBox:
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome(
            'C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe')
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        BMWRadioBtn = driver.find_element_by_id('bmwradio')
        BMWRadioBtn.click()
        time.sleep(2)

        BenzRadioBtn = driver.find_element_by_id('benzradio')
        BenzRadioBtn.click()
        time.sleep(2)

        BMWCheck = driver.find_element_by_id('bmwcheck')
        BMWCheck.click()
        time.sleep(2)

        BenzCheck = driver.find_element_by_id('benzcheck')
        BenzCheck.click()
        print("BMW  Radio Button is selected?" + str(BMWRadioBtn.is_selected())) # True if selected and False if not selected
        print("Benz Radio Button is selected?" + str(BenzRadioBtn.is_selected()))
        print("BMW  Check Box is selected?" + str(BMWCheck.is_selected()))
        print("Benz  Check Box is selected?" + str(BenzCheck.is_selected()))


ff = RadioButtonandCheckBox()
ff.test()
