"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 4단계 6번
"""

x = []

# x에 입력한 수 % 42한 값을 append
for a in range(10):
    b = int(input())
    c = b % 42
    x.append(c)

# x를 집합으로 => 집합은 중복된 수 계산 X
dif = set(x)

print(len(dif))
