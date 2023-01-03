"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 2단계 7번
"""

a, b, c = map(int, input().split())

d = [a, b, c]
e = int(max(d))

if d.count(a) == 3 :
    print(10000+(a*1000))
elif d.count(a) == 2 :
    print(1000+(a*100))
elif d.count(b) == 2 :
    print(1000+(b*100))
elif d.count(c) == 2 :
    print(1000+(c*100))
elif a != b != c :
    print(e*100)