import requests
from bs4 import BeautifulSoup

# naver 서버에 대화 시도
response = requests.get("https://www.naver.com")

# naver에서 html 줌
html = response.text

# html 번역 선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn인 거 한 개 찾아냄
word = soup.select_one('#NM_set_home_btn')

# text 요소만 출력
print(word.text)