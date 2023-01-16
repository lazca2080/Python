"""
날짜 : 2023/01/08
이름 : 박종협
내용 : 백준 4단계 9번
"""

C = int(input())
y = []

for a in range(C):
    total = 0
    caseAverage = 0
    count = 0

    N = list(map(int, input().split()))

    for b in N[1:]:
        total += b

    caseAverage = total/(len(N)-1)

    for c in N[1:]:
        if caseAverage < c:
            count += 1
    rate = count/len(N[1:])*100
    print(f'{rate:.3f}%')
    