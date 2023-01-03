"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 1단계 11번
"""

a = int(input())
b = int(input())

print((b%10)*a)
print(((b%100)//10)*a)
print((b//100)*a)
print(a*b)