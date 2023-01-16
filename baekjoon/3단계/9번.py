"""
날짜 : 2023/01/04
이름 : 박종협
내용 : 백준 3단계 9번
"""

a = int(input())

for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)