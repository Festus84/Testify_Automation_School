import time
from pom2_task import pom2_task
from pom3_task import pom3_task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_simplified = pom3_task()
    print(test_automation_simplified)
    switch_to_software_testing = pom2_task()
    print(switch_to_software_testing.text)
    # print(switch_to_testing.firstname_input, switch_to_testing.lastname_input)
    # contact_page.submit_button.click()
    time.sleep(20)


if __name__ == '__main__':
    main()
