from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXpathFormat:
    def XpathFormat(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome(
            "C:\\Users\\Bilal.Ikram\\PycharmProjects\\firstSeleniumTest\\venv\\selenium\\webdriver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        driver.find_element_by_link_text("Login").click()
        time.sleep(3)
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()
        driver.find_element(By.LINK_TEXT, "All Courses").click()
        time.sleep(3)

        # SearchCourse
        SearchBox = driver.find_element(By.ID, "search-courses")
        SearchBox.send_keys("JavaScript")

        # Select Course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)

        courseElement.click()
        time.sleep(3)


ff = DynamicXpathFormat()
ff.XpathFormat()
