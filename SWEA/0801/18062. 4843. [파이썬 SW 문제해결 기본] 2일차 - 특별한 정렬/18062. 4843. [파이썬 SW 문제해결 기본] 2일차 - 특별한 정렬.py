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
        for j in range(i, n):
            # 짝수 인덱스 : 최대값
            if i % 2 == 0 and numbers[j] > numbers[idx]:
                idx = j
            # 홀수 인덱스 : 최소값
            elif i % 2 == 1 and numbers[j] < numbers[idx]:
                idx = j
        numbers[i], numbers[idx] = numbers[idx], numbers[i]


    print(f'#{tc}', end = ' ')
    for num in numbers:
        print(num, end = ' ')
    print()