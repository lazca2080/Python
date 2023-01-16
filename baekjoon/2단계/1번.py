"""
날짜 : 2023/01/03
이름 : 박종협
내용 : 백준 2단계 1번
"""

a, b = map(int, input().split())

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')