from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

#유저 정보 넣기
options.add_argument(f"User-Agent={user}")

#화면 자동 종료 해제 옵션
options.add_experimental_option("detach",True)

#화면크기
# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
options.add_argument("window-size=500, 500")

#브라우저 화면이 나오지 않은 상태에서 크롤링 작업을 만들어주는 옵션
# options.add_argument("--headless")

#상단에 조작되고 있다는 메세지 지우는 옵션
options.add_experimental_option("excludeSwitches",["enable-automation"])

#음소거 옵션 추가
options.add_argument("--mute-audio")

#시크릿 모드
options.add_argument("incognito")


driver = webdriver.Chrome(options=options)
url = "https://www.naver.com"
driver.get(url)