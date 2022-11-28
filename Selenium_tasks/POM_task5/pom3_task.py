
from selenium.webdriver.common.by import By


class pom3_task:

    def _init_(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
