"""
날짜 : 2023/01/02
이름 : 박종협
내용 : 백준 6단계 8번
"""

Str = str(input())

alpha = [[3,"A","B","C"], [4,"D","E","F"], [5,"G","H","I"],
        [6,"J","K","L"], [7,"M","N","O"], [8,"P","Q","R","S"],
        [9,"T","U","V"], [10,"W","X","Y","Z"]]

Num = []
count = 0
total = 0

for b in Str:
        for a in alpha:
                try:
                        a.index(b)
                        break
                except:
                        pass
                count += 1
        Num.append(count)
        count = 0

for c in Num:
        total += alpha[c][0]
        
print(total)