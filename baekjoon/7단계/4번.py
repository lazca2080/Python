"""
날짜 : 2023/01/13
이름 : 박종협
내용 : 백준 7단계 4번
"""
import math

A, B, V = map(int, input().split())

print(math.ceil((V-A)/(A-B))+1)

# A B V
# 5 1 6

# (6-5)/4