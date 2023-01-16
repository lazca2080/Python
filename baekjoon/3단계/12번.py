"""
날짜 : 2023/01/04
이름 : 박종협
내용 : 백준 3단계 12번
"""

a = int(input())
ori = a
x, y, z, count = 0, 0, 0, 0

while True:
    x = a//10
    y = a%10

    if x+y < 10:
        count +=1
        a = (y*10)+(x+y)
    else:
        count +=1
        a = (y*10)+((x+y)%10)

    if ori == a:
        break

print(count)

