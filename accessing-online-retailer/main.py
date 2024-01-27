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
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")

    return driver

def main():
  driver = get_driver()

  #find and fiil in username and password
  driver.find_element(by="id", value="CustomerEmail").send_keys("app7flask@gmail.com")
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("??!65EhGMg8.WwY" + Keys.RETURN)
  time.sleep(2)

  #click on Home and wait for 2 sec
  driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  time.sleep(2)

  print(driver.current_url)

print(main())