from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def print_element_attributes(element):
    print("ID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("innerText"))
    print("Inner HTML:", element.get_attribute("innerHTML"))


def print_element_properties(element):
    print("Testify Limited", element.get_property("Testify Limited"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    testify_limited = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print("Testify Limited", testify_limited, testify_limited.text)
    print_element_attributes(testify_limited)
    print_element_properties(testify_limited)


if __name__ == '__main__':
    main()
