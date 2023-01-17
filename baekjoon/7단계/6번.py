"""
날짜 : 2023/01/17
이름 : 박종협
내용 : 백준 7단계 6번
"""

T = int(input())

for a in range(T):

    floor = int(input())
    roomNum = int(input())

    zeroF = [x for x in range(1, roomNum+1)]

    for b in range(floor):
        for c in range(1, roomNum):
            zeroF[c] = zeroF[c] + zeroF[c-1]

    print(zeroF[-1])