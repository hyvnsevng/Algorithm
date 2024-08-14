import sys

sys.stdin = open('4881_input.txt')

def backtrack(depth, temp):
    global min_sum

    if temp >= min_sum:
        return

    elif depth >= n:
        min_sum = temp
        return

    for i in range(n):

        if not visited[i]:
            num = matrix[depth][i]
            visited[i] = True
            temp += num
            backtrack(depth+1, temp)
            visited[i] = False
            temp -= num


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    visited = [False for _ in range(n)]
    min_sum = 987654321

    backtrack(0, 0)

    print(f'#{tc} {min_sum}')
