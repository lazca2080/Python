a ,b = map(int, input().split())

c = b - 45
d = a - 1

if d == 24 : 
    if c >= 0 :
        print('0', c)
    elif c < 0 :
        print('0', c+60)
elif d != 24 and d > 0 :
    if c >= 0 :
        print(a, c)
    elif c < 0 :
        print (d, c+60)
elif d <= 0 :
    if c >= 0 :
        print(d+24, c)
    elif c < 0 :
        print(d+24, c+60)