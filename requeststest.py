import requests

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}

url = "https://www.naver.com"

r = requests.get(url, headers=headers)

r.status_code