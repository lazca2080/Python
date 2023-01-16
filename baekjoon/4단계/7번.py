"""
날짜 : 2023/01/08
이름 : 박종협
내용 : 백준 4단계 7번
"""

# 과목수
N = int(input())

# 세준이의 원래 점수
x = list(map(int, input().split()))
# 세준이가 바꿀 점수
y = []

# 세준이의 원래 점수의 최대값
max = max(x)

# 세준이가 바꾼 점수의 토탈
total = 0

for a in x:
    # 최대값을 기준으로 바꿀 점수 append
    y.append(a/max*100)
    total += a/max*100

print(total/len(y))