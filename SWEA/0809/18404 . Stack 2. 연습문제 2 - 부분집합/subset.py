def subset(myset, idx, temp):
    global count

    if temp == 10:
        count += 1
        return

    elif temp > 10:
        return

    for i in range(idx, N):
        if not visited[i]:
            temp += myset[i]
            visited[i] = True
            subset(myset, i+1, temp)
            temp -= myset[i]
            visited[i] = False


# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):
    A = list(map(int, input().split()))     # 집합
    N = len(A)                              # 집합 요소 개수
    visited = [False for _ in range(N)]
    count = 0

    subset(A, 0, 0)
    print(count)
