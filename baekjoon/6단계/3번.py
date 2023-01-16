"""
날짜 : 2023/01/10
이름 : 박종협
내용 : 백준 6단계 3번
"""

S = str(input())
Alpah = [chr(x) for x in range(97, 123)]

for a in Alpah: 
    print(list(S).index(a) if a in list(S) else '-1', end=' ')

