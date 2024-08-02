
import sys

sys.stdin = open('4831_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    busstop = [0 for _ in range(N+1)]
    charger = list(map(int, input().split()))

    # busstop 리스트에 충전기 위치 표시
    for i in charger:
        busstop[i] = 1

    i = 0

    ans = 0
    while i+K < N:
        # print(busstop[i+K:i:-1])
        if 1 not in busstop[i+K:i:-1]:
            ans = 0
            break

        i += (K - busstop[i+K:i:-1].index(1))
        # print(i)
        ans += 1

    print(f'#{tc} {ans}')

