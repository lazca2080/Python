"""
날짜 : 2023/01/10
이름 : 박종협
내용 : 백준 6단계 1번
"""

N = input()

if type(N) == str :
    print(ord(N))
elif type(N) == int : 
    print(chr(N))