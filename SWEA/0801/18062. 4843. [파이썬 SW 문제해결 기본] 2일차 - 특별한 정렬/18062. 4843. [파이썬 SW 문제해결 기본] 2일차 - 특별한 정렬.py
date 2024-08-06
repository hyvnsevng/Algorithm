import sys

sys.stdin = open('4843_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    pass
    N = int(input())
    numbers = list(map(int, input().split()))

    n = len(numbers)

    for i in range(n - 1):
        idx = i     # 시작 인덱스
        for j in range(i+1, n):
            # 짝수 인덱스 : 최대값
            if not i % 2 and numbers[j] > numbers[idx]:
                idx = j
            # 홀수 인덱스 : 최소값
            elif i % 2 and numbers[j] < numbers[idx]:
                idx = j
        numbers[i], numbers[idx] = numbers[idx], numbers[i]


    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(numbers[i], end = ' ')
    print()