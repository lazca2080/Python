"""
날짜 : 2023/01/03
이름 : 박종협
내용 : 백준 2단계 3번
"""

a = int(input())

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) :
    print('1');
else :
    print('0')