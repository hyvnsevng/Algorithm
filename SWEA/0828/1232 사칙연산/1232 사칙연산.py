import sys

sys.stdin = open('input.txt')


def calculate(node):
    val = tree[node][0]
    l, r = tree[node][1], tree[node][2]  # l, r : 트리 위치
    if type(tree[l][0]) != int:
        tree[l] = calculate(l)
    if type(tree[r][0]) != int:
        tree[r] = calculate(r)

    if val =='+':
        tree[node] = [tree[l][0]+tree[r][0]]
    elif val == '-':
        tree[node] = [tree[l][0]-tree[r][0]]
    elif val == '*':
        tree[node] = [tree[l][0]*tree[r][0]]
    elif val == '/':
        tree[node] = [tree[l][0]//tree[r][0]]

    return tree[node]


# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    tree = [[] for _ in range(n+1)]

    for _ in range(n):
        lst = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        tree[lst[0]] = lst[1:]

    ans = calculate(1)[0]
    print(f'#{tc} {ans}')