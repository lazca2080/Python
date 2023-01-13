"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 10번
"""

N = int(input())
words = []
wordsSet = ()
count = 0
num = 0
numTotal = 0
total = 0
result = 0

for a in range(N):
    b = input()
    words.append(b)

for word in words:
    wordsSet = set(word)
    for alpha in list(wordsSet):
        # alpha 가 h일 때
        # count 1
        count = str(word).count(alpha)
        # alpha 가 h일 때 num이 연속하면 +1 연속하지않으면 = 0
        for i in range(len(str(word))):
            if alpha == word[i]:
                num +=1
                numTotal = num
            else:
                num = 0
        
        # count 값과 num이 일치하지 않는다 => 연속하지 않는 문자열
        if count != numTotal:
            total += 1

        count = 0
        num = 0
        numTotal = 0
    # total이 하나라도 잡힌다 => 해당 문자열은 연속하지않음
    if total == 0:
        result +=1
    total = 0

print(result)


        


    


