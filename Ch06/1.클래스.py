"""
날짜 : 2023/01/11
이름 : 박종협
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

sonata = Car('소나타', '흰색', 30000)

sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car('BMW', '검정색', 50000)

bmw.speedUp()
bmw.speedDown()
bmw.show()

nh = Account('농협', '215-4572-12321', '홍길동', 50000)

nh.deposit(20000)
nh.withdraw(10000)
# 캡슐화
# nh.__balance += 1
nh.show()

sh = Account('신한', '1553-721-45641', '홍홍홍', 30000)

sh.deposit(30000)
sh.withdraw(10000)
sh.show()