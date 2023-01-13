"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 7단계 1번
"""

N = list(map(int, input().split()))

# A = 고정 비용
A = N[0]
# B = 가변 비용
B = N[1]
# C = 판매 비용
C = N[2]

i = 0

while True:
    i += 1

    # 절대 수익이 날 수 없을 때
    # 가변비용이 판매 비용보다 더 비쌀 때
    if B >= C:
        print(-1)
        break
    else:
        N = A/(C-B)
        print(int(N+1))
        break
