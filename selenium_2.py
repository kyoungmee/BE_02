from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/home"

# req = requests.get(url)
# html = req.text
# print(html)
# JS로 구성된 부분이 많아서 soup으로 가지고 올수있는 정보가 거의 없음

driver = webdriver.Chrome()
driver.get(url) #req = requests.get(url)
html = driver.page_source #html = req.text
time.sleep(1)

print(html)