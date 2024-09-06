import sys

sys.stdin = open('5202_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    time = []
    n = int(input())
    for _ in range(n):
        lst = list(map(int, input().split()))
        time.append(lst)
    time = sorted(time, key=lambda x: x[1])

    prev = time[0]
    ans = 1
    for i in range(1, len(time)):
        if time[i][0] >= prev[1]:
           ans += 1
           prev = time[i]

    print(f'#{tc} {ans}')