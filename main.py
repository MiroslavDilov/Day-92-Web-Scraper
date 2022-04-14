from selenium import webdriver
from bs4 import BeautifulSoup
# import requests
import time

driver = webdriver.Chrome("D:\Chrome Driver\chromedriver.exe")

driver.get("https://steamdb.info/graph/")

select_button = driver.find_element(by='name', value='table-apps_length')
select_button.click()

all_button = driver.find_element(by='xpath', value='//*[@id="table-apps_length"]/label/select/option[7]')
all_button.click()


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('tr', class_='app')

for row in rows:
    # print(f"Name: {row.contents[5].a.contents[0]}" )
    name = row.contents[5].a.contents[0]
    current_players = row.contents[7].contents[0]
    twenty_four_hour_peak = row.contents[9].contents[0]
    all_time_peak = row.contents[11].contents[0]

    print(f"Name: {name}")
    print(f"Current Players: {current_players}")
    print(f"24 Hour Peak: {twenty_four_hour_peak}")
    print(f"All Time Peak: {all_time_peak}")
    print("=======")

driver.quit()