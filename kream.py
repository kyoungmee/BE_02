from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = Options()

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options)


url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(0.3)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(0.1)

for i in range(20):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    driver.save_screenshot(f"/Users/kyoungmee/Desktop/2024_BE/Crawling/kream_pic/supreme.png")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

num = 1
for i in items:
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text:
        brand = i.select_one(".product_info_product_name")
        #넘버 1부터 시작하세요
        print(f"[{num}]")
        print(f"제품명 : {brand.text}")
        print()
        num +=1
