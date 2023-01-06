"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 2번
"""

N = int(input())

n = int(input())

total = 0
for a in str(n):
    total += int(a)

print(total)