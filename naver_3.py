import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
search_url = input("검색어를 입력해주세요:")


url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

keyWord = soup.select(".keyword_box_wrap.type_color")

for i in keyWord :
    name = i.select_one(".name.elss")
    cat = i.select_one(".etc_area")
    tit = i.select_one(".title_link._cross_trigger._foryou_trigger")
    print(f"블로그 작성자는 : {name.text}")
    print(f"이블로거는 : {cat.text}")
    print(f"제목은 : {tit.text}")
    print()