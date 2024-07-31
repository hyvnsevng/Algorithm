import sys

sys.stdin = open('4837_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [x for x in range(1, 13)]
    n = len(A)

    answer = 0
    for i in range(1<<n):
        total = 0
        count = 0
        for j in range(n):
            if i&(1<<j):
                total += A[j]
                count += 1

        if count == N and total == K:
            answer += 1

    print(f'#{tc} {answer}')


'''
for i in range(2<<j):       # i:  n번째 부분집합,   j: 집합원소개수
'''