import sys
input = sys.stdin.readline


def str2int(ch):
    return ord(ch) - 65


def int2str(num):
    return chr(num + 65)


def solve(node):
    if node < 0:
        return
    left, right = edges[node]
    ch = int2str(node)
    ans[0].append(ch)
    solve(left)
    ans[1].append(ch)
    solve(right)
    ans[2].append(ch)


N = int(input())

edges = [(-1, -1) for _ in range(N)]
for _ in range(N):
    node, left, right = input().rstrip('\n').split(' ')
    edges[str2int(node)] = (str2int(left), str2int(right))
    
ans = [[], [], []]
solve(0)
for line in ans:
    print("".join(line))