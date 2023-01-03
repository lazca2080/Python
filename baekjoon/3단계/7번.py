"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 3단계 7번
"""

a = int(input())

x, y = 0, 0

for b in range(a):
    x, y = map(int, input().split())
    print(f'Case #{b+1}: {x} + {y} =',x+y)