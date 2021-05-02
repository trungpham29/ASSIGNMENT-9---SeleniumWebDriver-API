from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("https://itmscoaching.herokuapp.com/form?fbclid=IwAR1YYSIdGp7M8sTWrIdOpPbMqbSu7Ixo7vMtzn_iZk10XZhvfcWwDf4uOhk")

fname = driver.find_element_by_xpath("/html/body/div/form/div/div[1]/input")
fname.send_keys("Binh")
lname = driver.find_element_by_xpath("/html/body/div/form/div/div[2]/input")
lname.send_keys("Nguyen")
jobtitle = driver.find_element_by_xpath("/html/body/div/form/div/div[3]/input")
jobtitle.send_keys("Tester")

education = driver.find_element_by_xpath("/html/body/div/form/div/div[4]/div[4]/input").click()
sex = driver.find_element_by_xpath("/html/body/div/form/div/div[5]/div[3]/input").click()
year = driver.find_element_by_xpath("/html/body/div/form/div/div[6]/select")
year.send_keys("5-9")
dateofbirth = driver.find_element_by_xpath("/html/body/div/form/div/div[7]/input")
dateofbirth.send_keys("07/20/2011")

subm = driver.find_element_by_xpath("/html/body/div/form/div/div[8]/a").click()

driver.close()



