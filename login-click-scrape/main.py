from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# service = Service("C:\\Users\\LENOVO\\Documents\\Learning RPA\\chromedriver.exe")

def get_driver():
    #set options to make browser easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")

    return driver

def clean_text(text):
  """Extract only the temperature of text"""
  output = float(text.split(": ")[1])
  return output


def main():
  driver = get_driver()

  #find and fiil in username and password
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)

  #click on Home and wait for 2 sec
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2)

  #Sracape the temperature value
  text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
  time.sleep(2)
  return clean_text(text)


print(main())