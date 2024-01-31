from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = Options()

user = "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"
options.add_argument("user-agent="+ user)
options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches",["enable-automation"])


driver = webdriver.Chrome(options=options)

#크롤링 코드 작성
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)

if driver.current_url != url:
    driver.get(url)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

more_btn = driver.find_elements(By.CSS_SELECTOR,"#moreBtn")[1].click()
time.sleep(3)

#노래 순위, 제목, 가수이름, 추가로 가져올수있는 정보 가져오기

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

areas = soup.select(".list_item")

num = 1
for i in areas:
    rank = i.select_one(".ranking_num")
    if rank == None:
        continue
    else:
        title = i.select_one(".title.ellipsis")
        name = i.select_one(".name.ellipsis")
        print(f"[{num}위]")
        print(f"제목 : {title.text}".replace("\n","").replace('\t',''))
        print(f"가수 : {name.text}")
        print()

        num+=1



#Q1. 도대체 time.sleep 얼마나 걸어야 하나.. 어떨땐 잘 넘어가고 어떨때는 중간에 서는데.. 저걸 마냥 늘려야하나..?
#Q2. quit()이거 하면 크롬 종료된다고 하는데 언제까지 켜져있어야 하는 것이며, 왜 종료가 안되는가..?
