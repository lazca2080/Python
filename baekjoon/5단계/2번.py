"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 5단계 2번
"""

# 셀프 넘버 구하기
allNum = set(range(1, 10001))
calcNum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    calcNum.add(i)

selfNum = sorted(allNum - calcNum)

for i in selfNum:
    print(i)


"""
# 생성자 구하기
def solve(x):
    List = set()
    num = list(map(int, str(x)))
    selfNum = x
    for a in num:
        selfNum += a

    if selfNum > 10000:
        return
    List.add(selfNum)
    return List

for z in range(1,10001):
    solve(z)
"""


"""
# 셀프 넘버 구하기
def selfNum(X):
    realNum = 0
    selfNum = X-18
    for a in range (2,19):
        Y = X-a
        print('1 : ',Y)
        realNum = Y
        num = list(map(int, str(Y)))
        print('2 : ',num)
        for b in num:
            realNum += b
        
        if X == realNum:
            print('3 : ',realNum)
            break
    

    return Y

print(selfNum(39))
"""