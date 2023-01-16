"""
날짜 : 2023/01/16
이름 : 박종협
내용 : 파이썬 Crawling 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 첫번째 시트 활성화
sheet = workbook.active
sheet['A1'] = '네이버 뉴스 :: IT/과학'
sheet['A2'] = '번호'
sheet['B2'] = '제목'
sheet['C2'] = '링크'

pg = 1
count = 1

while True:

    # HTML 요청
    url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20230116&page=%d" % pg
    html = req.get(url, headers={'User-Agent' : 'Mozilla/5.0'}).text

    # print(html)

    # 문서 객체 생성
    dom = bs(html, 'html.parser')

    # 데이터파싱
    tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text

    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')
    currentPg = dom.select_one('#main_content > div.paging > strong').text

    if int(currentPg) != pg : break

    #if prelis == lis: break

    # 출력
    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href = tag_a['href']

        print('count :',count)
        print('title :',title.strip())
        print('href :',href.strip())
        sheet.append([count, title.strip(), href.strip()])

        count += 1

    pg += 1

# 저장닫기
workbook.save('C:/Users/java2/Desktop/news.xlsx')
workbook.close()

print('프로그램 종료...')