import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://www.melon.com/chart/month/index.htm"
req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lstAll = soup.find_all(class_ = ["lst50", "lst100"])


num = 1

for i in lstAll:
    title = i.select_one(".ellipsis.rank01")
    name = i.select_one(".checkEllipsis")
    rank = i.select_one(".rank_wrap")
    rank_up = i.select_one(".up")
    rank_now = i.select_one(".rank")

    if "상승" in rank.text:
        print(f"'{name.text}'의 '{title.text}' [{rank_up.text}]단계 상승 / {rank_now.text}위 (2023.12)".replace('\n',''))
        print ()
        num +=1
    
print (f"총 {num}개의 상승 변등 곡이 있습니다.")

