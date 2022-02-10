import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
rse = requitst.get(url)

res.raise_for_status() #문제 있을 시 종료

soup = BeautifulSoup(res.text,"lxml")
print(soup.title)
