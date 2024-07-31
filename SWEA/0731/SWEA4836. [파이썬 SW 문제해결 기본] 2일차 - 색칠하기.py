import sys

sys.stdin = open('4836_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())

    graph = [[0 for _ in range(10)] for _ in range(10)]
    coloring = [list(map(int, input().split())) for i in range(N)]

    answer = 0

    for color_info in coloring:
        r1, c1, r2, c2, color = color_info

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                graph[row][col] += color
                if graph[row][col] == 3:
                    answer += 1


    print(f'#{tc} {answer}')