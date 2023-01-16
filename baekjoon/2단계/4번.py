"""
날짜 : 2023/01/03
이름 : 박종협
내용 : 백준 2단계 4번
"""

a = int(input())
b = int(input())

if a > 0 and b > 0 :
    print('1')
elif a < 0 and b > 0 :
    print('2')
elif a < 0 and b < 0 :
    print('3')
else :
    print('4')