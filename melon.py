import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100

lst_all = soup.find_all(class_=["lst50","lst100"])

for rank,i in enumerate(lst_all,1):
    # rank = i.select_one(".rank")
    title = i.select_one(".ellipsis.rank01")
    singer = i.select_one(".ellipsis.rank02 a") 
    #같은 클래스 네임일때는 . 으로 연결 // 그 안에 자식요소일경우 띄어쓰기로 
    album = i.select_one(".ellipsis.rank03 a")


    print(f"{rank}위")
    print(f"제목 : {title.text.strip()}")
    print(f"가수 : {singer.text}")
    print(f"앨범 : {album.text}")
    print()

print(len(lst_all))