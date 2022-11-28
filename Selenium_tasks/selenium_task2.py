from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_xpath(driver):
    explore_element = driver.find_element(By.XPATH,
                                          '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button/span[1]')
    print("Explore Element", explore_element, explore_element.text)


def locate_by_xpath(driver):
    subscribe_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[11]/div/div/div[1]/h2')
    print("Subscribe_Element", subscribe_element, subscribe_element.text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_xpath(driver)
    locate_by_xpath(driver)


if __name__ == '__main__':
    main()
