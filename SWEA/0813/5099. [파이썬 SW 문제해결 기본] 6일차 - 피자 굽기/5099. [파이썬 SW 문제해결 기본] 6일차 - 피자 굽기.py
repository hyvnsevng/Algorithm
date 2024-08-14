import sys

sys.stdin = open('5099_input.txt')

T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n, m = map(int, input().split())
    C = list(map(int, input().split()))

    queue = [[] for _ in range(n)]
    front = 0
    rear = -1

    idx = 0
    while True:
        if idx < n:
            queue[idx] = [C[idx], idx]
            rear = (rear + 1) % n
            idx += 1
        elif (rear + 1) % n == front and idx < m:
            melt = queue[front][0] // 2
            if melt == 0:
                queue[front] = [C[idx], idx]
                idx += 1
            else:
                queue[front][0] = melt
            rear = (rear + 1) % n
            front = (front + 1) % n
        else:
            if len(queue) == 1:
                break
            if queue[front]:
                melt = queue[front][0] // 2
                if melt == 0:
                    queue.pop(front)
                else:
                    queue[front][0] = melt

            front = (front + 1) % n % len(queue)

        print(queue, front, rear)

    print(f'#{tc} {queue[0][1] + 1}')