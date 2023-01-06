"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 5번
"""

Alpha = str(input()).upper()
overlapAlpah = list(set(Alpha))
countList = []

for a in overlapAlpah:
    count = Alpha.count(a)
    countList.append(count)

if countList.count(max(countList)) > 1:
    print('?')
else :
    print(overlapAlpah[countList.index(max(countList))])