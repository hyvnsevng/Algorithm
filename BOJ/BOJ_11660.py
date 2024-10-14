# 백준 11660번 구간 합 구하기 5

# 2차원 배열의 구간합 구하는 문제
# 각 열에 대해 1차원 배열의 구간합 문제와 같이 풀이하였다.

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
new_graph = [[0]*(n+1) for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_graph[i][j+1] = new_graph[i][j] + graph[i][j]

for tc in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = 0

    for i in range(x1-1, x2):
        ans += (new_graph[i][y2] - new_graph[i][y1-1])

    print(ans)