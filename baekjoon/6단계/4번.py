"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 4번
"""

T = int(input())

for a in range(T):
    R, S = list(map(str, input().split()))

    for b in S:
        print(b*int(R), end='')
    print('')