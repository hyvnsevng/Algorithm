import sys
from collections import deque

sys.stdin = open('sample_input (2).txt')

def calculation(n, m):
    queue = deque()
    queue.append((n, 0))
    visited = [False] * 1000001
    while queue:
        num, calc = queue.popleft()
        if num == m:
            return calc
        a, b, c, d = num + 1, num - 1, num * 2, num - 10

        if 1000000 >= a > 0 and not visited[a]:
            queue.append((a, calc + 1))
            visited[a] = True
        if 1000000 >= b > 0 and not visited[b]:
            queue.append((b, calc + 1))
            visited[b] = True
        if 1000000 >= c > 0 and not visited[c]:
            queue.append((c, calc + 1))
            visited[c] = True
        if 1000000 >= d > 0 and not visited[d]:
            queue.append((d, calc + 1))
            visited[d] = True

    return 0


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{tc} {calculation(n, m)}')
