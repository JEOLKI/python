# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request


client_id = "06IaFp7HOI08Va_qibuP"
client_secret = "lhtSbU3LQI"
encText = urllib.parse.quote("대전대흥동맛집")
url = "https://openapi.naver.com/v1/search/local.xml?display=5&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    
    
## parser.py
from bs4 import BeautifulSoup

## HTML 소스 가져오기
html = response_body.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

items = soup.select(
    'item'
    )

for item in items:
    print(item)

# DB저장
import sqlite3

conn = sqlite3.connect("naver.db", isolation_level=None)

cursor = conn.cursor()

sql = "insert into naver (title,link,category,description,telephone,address,roadAddress,mapx,mapy) values(?,?,?,?,?,?,?,?,?)"

for item in items:
    data=(item.title.text,
          item.link.text,
          item.category.text,
          item.description.text,
          item.telephone.text,
          item.address.text,
          item.roadaddress.text,
          item.mapx.text,
          item.mapy.text)
    cursor.execute(sql,data)

#conn.commit()
conn.close()





