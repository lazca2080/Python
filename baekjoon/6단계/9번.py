"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 9번
"""

Alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

Str = input()

for a in Alpha:
    Str = Str.replace(a, ",")

print(len(Str))
