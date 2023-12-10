from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\\Users\\LENOVO\\Documents\\Learning RPA\\chromedriver.exe")

def get_driver():
    #set options to make browser easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")

    return driver


def main():
  driver = get_driver()
  element = driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  element = driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)


print(main())