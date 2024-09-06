import sys

sys.stdin = open('input.txt')


def max_p(p, depth):
    global ans

    if p <= ans:
        return

    if depth == len(task):
        ans = p
        return

    for i in range(len(task)):
        if i not in task:
            task[depth] = i
            tmp = prob[depth][i]
            max_p(p*tmp/100, depth + 1)
            task[depth] = -1


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    ans = 0
    prob = [list(map(int, input().split())) for _ in range(n)]
    task = [-1 for _ in range(n)]
    max_p(1, 0)

    print(f'#{tc} {ans*100:.6f}')