"""
날짜 : 2023/01/11
이름 : 박종협
내용 : 파이썬 상속 실습하기
"""
from sub1.StockAccount import StorckAccount

kb = StorckAccount('KB증권', '123-456-789', '홍길동', 50000, '삼성전자', 10, 60000)
kb.deposit(1000000)
kb.sell(5, 65000)
kb.show()
