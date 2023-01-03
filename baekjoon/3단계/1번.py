"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 3단계 1번
"""

a = int(input())

b = 1

while b <= 9 : 
    print(f'{a} * {b} =', a*b)
    b += 1

for b in range(1, 10):
    print(f'{a} * {b} =', a*b)
