import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://www.naver.com/"
search_url = input("검색어를 입력해주세요:")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

soup.find(class_='link_service', text="뉴스") #select_one
soup.find_all(id = 'link_service') #select