import sys
from collections import deque

sys.stdin = open('5097_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    numbers = deque(list(map(int, input().split())))

    for i in range(m):
        numbers.append(numbers.popleft())

    print(f'#{tc} {numbers[0]}')

