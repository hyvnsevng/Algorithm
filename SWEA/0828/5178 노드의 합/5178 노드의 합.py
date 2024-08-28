import sys

sys.stdin = open('5178_input.txt')


def sum_of_tree(node):
    leftnode = node * 2
    rightnode = node * 2 + 1

    if rightnode >= len(tree):  # 자식 노드가 한 쪽만 있는 경우
        return tree[leftnode]

    if not tree[leftnode]:      # 왼쪽 자식 노드가 비어있을 경우
        left = sum_of_tree(leftnode)    # 왼쪽 자식 노드의 자식 노드를 확인하여 합을 구한다.
    else:
        left = tree[leftnode]

    if not tree[rightnode]:     # 오른쪽 자식 노드에 대해서도 동일하게 진행
        right = sum_of_tree(rightnode)
    else:
        right = tree[rightnode]

    result = left + right
    return result


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())

    tree = [0 for _ in range(n+1)]

    for _ in range(m):
        i, num = map(int, input().split())
        tree[i] = num

    print(sum_of_tree(l))


