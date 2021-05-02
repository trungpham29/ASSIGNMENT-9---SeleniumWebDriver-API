from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("http://practice.automationtesting.in/")

login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
email = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[1]/input")
email.send_keys("tp012341@gmail.com")
passw = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[2]/input")
passw.send_keys("Trung090909!")

res = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]").click()

driver.close()


