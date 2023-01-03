import sys

"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 3단계 5번
"""

a = int(input())

x, y = 0,0

for b in range(a):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)