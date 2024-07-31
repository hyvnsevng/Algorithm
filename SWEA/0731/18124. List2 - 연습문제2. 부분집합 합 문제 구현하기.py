import sys

sys.stdin = open('iinput.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    n = len(nums)

    count = 0
    for i in range(1, 1<<n):
        total = 0
        for j in range(n):
            if i&(1<<j):
                total += nums[j]
        if total == 0:
            count += 1
            break



    print(f'#{tc} {count}')