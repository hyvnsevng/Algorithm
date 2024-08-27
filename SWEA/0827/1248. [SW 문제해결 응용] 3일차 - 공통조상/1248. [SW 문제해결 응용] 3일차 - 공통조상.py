import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    v, e, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))

    parents = [0 for _ in range(max(edges)+1)]
    tree = [[] for _ in range(max(edges)+1)]

    for i in range(0, len(edges), 2):
        parents[edges[i+1]] = edges[i]
        tree[edges[i]].append(edges[])

    # print(parents)

    parents1, parents2 = [node1], [node2]
    n1, n2 = node1, node2

    while n1:
        n1 = parents[n1]
        parents1.append(n1)

    while n2:
        n2 = parents[n2]
        parents2.append(n2)

    nearest = max(set(parents1) & set(parents2))

    size = 1

    for node in parents1:
        if node > nearest:
            size += 1

    for node in parents2:
        if node > nearest:
            size += 1

    print(parents1, parents2)

    print(f'#{tc} {nearest} {size}')

