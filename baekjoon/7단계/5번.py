"""
날짜 : 2023/01/13
이름 : 박종협
내용 : 백준 7단계 5번
"""

T = int(input())

for a in range(T):
    H, W, N = map(int, input().split())
    roomNum = str((N%H)*10)
    roomNum2 = str(N//H+1)
    print(int(roomNum+roomNum2))
            