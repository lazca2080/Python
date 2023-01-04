"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 4단계 4번
"""

num = []

for a in range(9):
    x = int(input())
    num.append(x)

print(max(num))
print(num.index(max(num))+1)