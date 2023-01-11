"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 10번
"""

N = int(input())
words = []
wordsSet = ()
count = 0
total = 0
num = 0
numTotal = 0

for a in range(N):
    b = input()
    words.append(b)

for word in words:
    wordsSet = set(word)
    for alpha in list(wordsSet):
        count = word.count(alpha)
        total += count
        for x in range(len(str(word))):
            if alpha == word[x]:
                num += 1
                numTotal += num
            else:
                num = 0
                numTotal += 0

print(total)
print(numTotal)
