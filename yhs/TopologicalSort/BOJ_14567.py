def dp(k):
    if not k:       # 0번 과목 존재하지 않으므로 0 반환
        return 0
    else:
        if not indegree[k]:     # memoization
            semester = max(map(dp, table[k]))   # 선수과목들의 이수 학기 중 최대값
            indegree[k] = semester + 1
        return indegree[k]


n, m = map(int, input().split())
table = [[0] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    table[b].append(a)      # table[b] : b의 선수과목 리스트

indegree = [0] * (n+1)  # i번 과목을 이수할 수 있는 학기
for i in range(n+1):
    dp(i)

print(*indegree[1:])    # 1~n번 과목의 이수 학기 출력
