from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com")

authentication = driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[21]/a").click()
username = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[1]/div/input")
username.send_keys("tomsmith")
passw = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[2]/div/input")
passw.send_keys("SuperSecretPassword!")

log = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button/i").click()

get_title = driver.title
print(get_title)

driver.close()


