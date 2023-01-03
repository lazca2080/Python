"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 2단계 5번
"""

a , b = map(int, input().split())

c = a-1
d = b-45

if b - 45 < 0 :
    if a == 0 :
        print('23', (b-45)+60)
    else :
        print(c, (b-45)+60)
else :
    print(a, d)


h, m = map(int, input().split())

h = h + (m-45)//60

if h < 0 : h += 24

if m - 45 < 0 : m = (m-45)+60
else : m = m-45    

print(h, m)

