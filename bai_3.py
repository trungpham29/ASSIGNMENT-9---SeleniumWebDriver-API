from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1920, 1080)
driver.close()



