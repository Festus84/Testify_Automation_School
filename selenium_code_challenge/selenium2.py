import time

import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from Selenium_tasks.task4 import send_keys_to_element


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    send_keys_to_element(driver.find_element(By.CLASS_NAME, "gLFyf"), "python")
    keyboard.press_and_release('enter')
    time.sleep(10)
    wikipedia_python_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')

    print("Wikipedia Brief:", wikipedia_python_text, wikipedia_python_text.text)

    time.sleep(10)

    driver.close()


main()
