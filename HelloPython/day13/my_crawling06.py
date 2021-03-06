# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request

## parser.py
from bs4 import BeautifulSoup

# DB저장
import sqlite3

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
    
## HTML 소스 가져오기
soup = BeautifulSoup(response_body, 'xml')

myitems = soup.select(
    'item'
    )

conn = sqlite3.connect("naver.db", isolation_level=None)

cursor = conn.cursor()

sql = "insert into naver (title,link,category,description,telephone,address,roadAddress,mapx,mapy) values(?,?,?,?,?,?,?,?,?)"

for item in myitems:
    title = item.find('title').text
    link = item.find('link').text
    category = item.find('category').text
    description = item.find('description').text
    telephone = item.find('telephone').text
    
    address = item.find('address').text
    roadAddress = item.find('roadAddress').text
    mapx = item.find('mapx').text
    mapy = item.find('mapy').text
    
    cursor.execute(sql,(title,link,category,description,telephone,address,roadAddress,mapx,mapy))

#conn.commit()
conn.close()





