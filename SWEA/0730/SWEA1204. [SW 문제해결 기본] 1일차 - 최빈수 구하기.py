def chlqls(arr):
    count = [0 for _ in range(101)]
    for num in arr:
        count[num] += 1

    Mcnt = count[0]
    result = 0

    for i in range(100, -1, -1):
        if Mcnt < count[i]:
            Mcnt = count[i]
            result = i

    return result


import sys

sys.stdin = open('input_1.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    testcase = int(input())
    numbers = list(map(int, input().split()))

    ans = chlqls(numbers)
    print(f'#{testcase} {ans}')