"""
날짜 : 2023/01/04
이름 : 박종협
내용 : 백준 3단계 2번
"""

a = int(input())

x, y = 0, 0

for b in range(a):
    x , y = map(int, input().split())
    print(x+y)
