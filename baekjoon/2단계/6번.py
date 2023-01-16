"""
날짜 : 2023/01/03
이름 : 박종협
내용 : 백준 2단계 6번
"""

h, m = map(int, input().split())
n = int(input())

h = h + (m+n)//60
m = (m+n)%60

if h >=24 : h -= 24

print(h , m)
