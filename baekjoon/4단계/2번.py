"""
날짜 : 2023/01/08
이름 : 박종협
내용 : 백준 4단계 2번
"""

x, y = map(int, input().split())

num = list(map(int, input().split()))

for a in range(x):
    if num[a] < y:
        print(num[a], end=' ')


"""
num.sort()

for a in range(num.index(y)):
    print(num[a], end=' ')
"""