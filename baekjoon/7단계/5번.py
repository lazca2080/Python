"""
날짜 : 2023/01/17
이름 : 박종협
내용 : 백준 7단계 5번
"""

T = int(input())

for a in range(T):
    H, W, N = map(int, input().split())

    floor = N%H
    roomNum = N//H + 1

    if N%H == 0:
        floor = H
        roomNum = N//H

    print(floor*100+roomNum)
            