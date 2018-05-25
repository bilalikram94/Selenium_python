from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Calendar_Selection:
    def DateSelection(self):
        baseURL = "http://www.expedia.com"
        driver = webdriver.Chrome("C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Clicks Flights Tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        print("Element found")

        # Find Departing Field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        print("Element Found")

        dateToSelect = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]//button[@class='datepicker-cal-date'][contains(text(),'31')]")
        print("date found")
        # Click The Date
        dateToSelect.click()
        print("Date Clicked")



        time.sleep(3)
        driver.quit()

    def DateSelection2(self):
        baseURL = "http://www.expedia.com"
        driver = webdriver.Chrome(
            "C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Clicks Flights Tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        print("Element found")

        # Find Departing Field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        print("Element Found")
        calMonth = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        calMonth.click()
        AllInvalidDates = calMonth.find_elements(By.TAG_NAME, "span")
        length = len(AllInvalidDates)
        print("No of invalid dates:" + str(length))


ff = Calendar_Selection()
ff.DateSelection2()


