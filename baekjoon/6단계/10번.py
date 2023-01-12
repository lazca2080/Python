"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 10번
"""

N = int(input())
words = []
wordsSet = ()
num = 0
numTotal = 0
count = 0
countTotal = 0

for a in range(N):
    b = input()
    words.append(b)

for word in words:
    wordsSet = set(word)
    for x in word:
        i = 0
        if word[i] == word[i+1]:
            num += 1
            numTotal += num
        elif i == len(str(word)):
            if word[i] == word[0]:
                num += 1
                numTotal += num

    for alpha in list(wordsSet):
        count = list(word).count(alpha)
        countTotal += count
    

        


    


