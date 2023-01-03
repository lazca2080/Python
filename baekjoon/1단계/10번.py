"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 1단계 10번
"""

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(int(((A%C) * (B%C))%C))