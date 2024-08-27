import sys

sys.stdin = open('5174_input.txt')

def visit(node):
    global ans

    if node:
        ans += 1

    for child_node in child[node]:
        visit(child_node)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))

    child = [[] for _ in range(1002)]       #

    for i in range(0, e*2, 2):
        child[lst[i]].append(lst[i+1])

    ans = 0
    visit(n)

    print(f'#{tc} {ans}')