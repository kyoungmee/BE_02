import requests
from bs4 import BeautifulSoup

#접속하고자 하는 주소 입력 => url
url = "https://www.naver.com"

#get 방식을 이용해서 서버에게 Resource(자원 = html,css,js)을 보내도록 요청. 데이터 수신이 가능하게 준비
#requests의 경우 거의 처음에 사용되고 이후에는 잘 사용되지 않음. 왜냐하면 정적인 사이트에서는 HTML코드가 변하지 않기때문
#request로 넘어오는 내용은 예를들어 네이버 화면에서 오른쪽클릭 -> 페이지 소스보기 로 보이는 내용과 동일
req = requests.get(url)
# print(req)

#get방식을 통해서 가져온 많은 데이터 중 우리가 필요한건 텍스트 형태의 자료(가장중요한 html포함)
html = req.text
# print(html)

#BeautifulSoup이라는 함수에는 2가지 파라미터를 넣는데 html, "html.parser"를 넣는다
#넣으면 파서(컴퓨터가 이해할수있도록 html 분해해서 트리구조로 변경하는것)가 진행된다
soup = BeautifulSoup(html, "html.parser")

#select_one 원하는 태그를 찾을수있는데 기준은 클래스명, id 태그도 가능. 
#클래스의 경우 앞에 (.), id는 앞에 (#)
query = soup.select_one("#query")
print(query)