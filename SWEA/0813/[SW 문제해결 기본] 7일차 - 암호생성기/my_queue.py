import sys
from collections import deque

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    _ = int(input())
    queue = deque(list(map(int, input().split())))

    while queue[-1]:
        for i in range(1, 6):
            num = queue.popleft()
            if num - i <= 0:
                queue.append(0)
                break
            else:
                num -= i
                queue.append(num)


    print(f'#{tc}', end = ' ')
    for password in queue:
        print(password, end = ' ')
    print()
