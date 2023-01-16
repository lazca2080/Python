"""
날짜 : 2023/01/09
이름 : 박종협
내용 : 백준 5단계 3번
"""

def han(n):
    num = []
    numlen = 0
    hansu = 0

    for a in str(n):
        num.append(int(a))

    numlen = len(num)

    if numlen == 3 and num[2]-num[1] == num[1]-num[0]:
        hansu = 1
    elif numlen == 4 and num[3]-num[2] == num[2]-num[1] == num[1]-num[0]:
        hansu = 1
    elif numlen <= 2:
        hansu = 1

    return hansu
        
n = int(input())
total = 0

for a in range(1,n+1):
    total += han(a)

print(total)
