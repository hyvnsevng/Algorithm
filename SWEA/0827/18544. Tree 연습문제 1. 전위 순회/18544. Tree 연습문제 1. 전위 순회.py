import sys

sys.stdin = open('input.txt')

def visit(node):
    if node:
        print(node, end=' ')
    for child in adj_lst[node]:
        visit(child)


# Testcase 수
n = int(input())
lst = list(map(int, input().split()))
adj_lst = [[] for _ in range(n+1)]

for i in range(0, len(lst), 2):
    adj_lst[lst[i]].append(lst[i+1])

visit(1)

