from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("https://steamdb.info/graph/")

# print(driver.find_element(by='tag_name', value='tbody'))
time.sleep(3)
print(driver.find_element(by='class', value='app'))