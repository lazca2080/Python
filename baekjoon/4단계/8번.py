"""
날짜 : 2023/01/08
이름 : 박종협
내용 : 백준 4단계 8번
"""

# 테스트 케이스의 개수
N = int(input())

# count
count = 0
# 총합
total = 0

# 테스트 케이스 만큼 반복
for a in range(N):
    x = input()
    # x의 길이만큼 반복
    for b in range(len(x)):
        # x를 리스트로 저장함 -> ex ) OOXXOOX > ['O', 'O', 'X', 'X', 'O', 'O', 'X']
        y = list(x)
        # O인지 X인지 비교 O이면 count++, +total, x이면 count = 0
        if y[b] == 'O':
            count += 1
            total += count
        elif y[b] == 'X' :
            count = 0
    # 처음 입력한 OX결과 끝났으므로 초기화 해줌
    print(total)
    count = 0
    total = 0

