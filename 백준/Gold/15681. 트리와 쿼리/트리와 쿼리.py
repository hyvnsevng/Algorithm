import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = [0] * (n+1)


def makeTree(node, parent):
    tree[node] = 1
    for child in edges[node]:
        if child == parent:
            continue
        tree[node] += makeTree(child, node)
    
    return tree[node]


edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

makeTree(r, -1)
for _ in range(q):
    query = int(input())
    print(tree[query])
