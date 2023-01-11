"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 7번
"""

N = list(map(int, input().split()))

x = str(N[0])[::-1]
y = str(N[1])[::-1]

if x > y:
    print(x)
elif x < y:
    print(y)