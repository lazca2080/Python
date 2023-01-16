"""
날짜 : 2023/01/04
이름 : 박종협
내용 : 백준 3단계 10번
"""

while True :
    x, y = map(int, input().split())
    if( x == 0 and y == 0):
        break
    print(x+y)