import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    txtusername = (driver.find_element(By.ID, "email"))
    txtusername.send_keys("08085461283")

    txtpasswd = (driver.find_element(By.ID, "pass"))
    txtpasswd.send_keys("Adewale1234@")

    driver.find_element(By.NAME, "login").click()
    # btnlogin.submit()

    time.sleep(10)


if __name__ == '__main__':
    main()
