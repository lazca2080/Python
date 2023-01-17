"""
날짜 : 2023/01/17
이름 : 박종협
내용 : 백준 7단계 7번
"""

N = int(input())

A = N/5+(N%5)/3
B = N/5
C = N/3
D = N/3+(N%3)/5

count = [A, B, C, D]
intCount = []

for a in count:
    print(a)
    if type(a) == int:
        intCount.append(a)

print(intCount)


    
