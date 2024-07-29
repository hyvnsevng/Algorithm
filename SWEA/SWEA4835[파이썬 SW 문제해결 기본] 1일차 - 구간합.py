import sys
sys.stdin = open("4835_input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    a = list(map(int, input().split()))

    # 최대/최소 구간합 초기화
    max_sum = 0
    min_sum = 0
    for _ in range(M):
        max_sum += a[_]
        min_sum += a[_]

    for i in range(N-M+1):
        sum_val = 0

        for num in a[i:i+M]:        # 현재 구간합
            sum_val += num

        if sum_val > max_sum:           # 최대 구간합
            max_sum = sum_val
        if sum_val < min_sum:           # 최소 구간합
            min_sum = sum_val

    print(f'#{test_case} {max_sum-min_sum}')




