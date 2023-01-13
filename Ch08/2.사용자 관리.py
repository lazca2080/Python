"""
날짜 : 2023/01/13
이름 : 박종협
내용 : 파이썬 사용자 관리 프로그램 실습하기
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='java2db', charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        break
    elif answer == 1:
        print('아이디, 이름, 휴대폰, 나이 순으로 입력하세요')
        user = list(map(str, input().split()))

        try:
            sql = "INSERT INTO `user3` VALUES('%s','%s','%s','%s')" % (user[0], user[1], user[2], user[3])
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()
        except:
            print('다시 시도해주세요!...')
            conn.close()

        print('등록 완료!...')

    elif answer == 2:
        sql = "SELECT * FROM `user3`"
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        for list in cur.fetchall():
            print('.................')
            print('아이디 : ', list[0])
            print('이름 : ', list[1])
            print('휴대폰 : ', list[2])
            print('나이 : ', list[3])
            print('조회 완료!...')
        conn.close()
        
    elif answer == 3:
        print('검색하고자 하는 이름을 입력하세요.')
        name = str(input())

        try:
            sql = "SELECT * FROM `user3` WHERE `name`='%s'" % (name)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

            for list in cur.fetchall():
                print('.................')
                print('아이디 : ', list[0])
                print('이름 : ', list[1])
                print('휴대폰 : ', list[2])
                print('나이 : ', list[3])
                
            print('조회 완료!...')
        except:
            print('일치하는 유저가 없습니다...')
            conn.close()

        conn.close()

    elif answer == 4:
        print('삭제하고자 하는 아이디를 입력하세요.')
        user = str(input())
        try:
            sql = "DELETE FROM `user3` WHERE `uid`='%s'" % (user)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except:
            print('일치하는 유저가 없습니다...')

        print('삭제 완료!...')
        conn.close()
    else:
        print('0 ~ 4 중에 입력하세요')
        

# 데이터베이스 종료
conn.close()
print('프로그램 종료...')