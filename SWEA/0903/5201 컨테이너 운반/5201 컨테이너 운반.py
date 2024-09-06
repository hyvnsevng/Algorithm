import sys

sys.stdin = open('5201_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())))

    ans = 0
    for weight in w:
        if t and weight <= t[-1]:
            t.pop()
            ans += weight

    print(f'#{tc} {ans}')