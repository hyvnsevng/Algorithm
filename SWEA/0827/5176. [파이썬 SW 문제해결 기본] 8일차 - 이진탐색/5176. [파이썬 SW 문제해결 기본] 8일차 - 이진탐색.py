# 중위 순회 구현 (이진트리구조)

import sys

sys.stdin = open('5176_input.txt')


def inorder_traverse(node, n):
    if node > n:
        return

    inorder_traverse(node*2, n)    # 왼
    visit(node)                 # 본인
    inorder_traverse(node*2+1, n)  # 오


def visit(node):
    global num

    binary_tree[node] = num
    num += 1


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())

    binary_tree = [0 for _ in range(n+1)]
    num = 1
    inorder_traverse(1, n)

    root = binary_tree[1]
    val = binary_tree[n//2]

    print(f'#{tc} {root} {val}')
