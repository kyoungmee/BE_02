from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query="
search_url = input("검색어를 입력해주세요:")

url = base_url + search_url

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

#스크롤 코드
# driver.execute_script("window.scrollTo(0,4000)")
# time.sleep(2)

#스크롤 끝까지 내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(4)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

area = soup.select(".view_wrap")

num = 1
for i in area :
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else : 
        title = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".user_info > a")
        print(f"[{num}]")
        print(f"포스팅 제목 : {title.text}")
        print(f"포스팅 작성자 : {name.text}")
        print(f"포스팅 링크 : {title['href']}")
        print()
        
        num +=1

