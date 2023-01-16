"""
날짜 : 2023/01/08
이름 : 박종협
내용 : 백준 4단계 5번
"""

x = []
y = []

# 1번부터 30번까지 등록
for a in range(30):
    x.append(a+1)

# 제출한 사람 찾기
for b in range(28):
    c = int(input())
    y.append(c)

# 리스트를 집합으로 변경 후 차집합 이용
who = set(x)-set(y)

# 최소 최대 출력
print(min(who), max(who))