"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 4단계 3번
"""

a = int(input())

num = list(map(int, input().split()))

num.sort()

print(num[0], num[a-1])