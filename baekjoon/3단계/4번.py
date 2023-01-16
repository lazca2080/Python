"""
날짜 : 2023/01/04
이름 : 박종협
내용 : 백준 3단계 4번
"""

a = int(input())
b = int(input())

x, y = 0,0
total = 0

for c in range(b):
    x, y = map(int, input().split())
    total += x*y

if a == total :
    print('Yes')
else :
    print('No')