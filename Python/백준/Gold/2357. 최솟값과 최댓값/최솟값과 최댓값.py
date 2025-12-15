import sys
input = sys.stdin.readline
# input = open('input.txt', 'r').readline
INF = 1000000000

N, M = map(int, input().split())

nums = [0] + [int(input()) for _ in range(N)]
max_tree = [0] * (4 * N)
min_tree = [0] * (4 * N)


def init(idx, start, end):
    if start == end:
        min_tree[idx] = nums[start]
        max_tree[idx] = nums[start]
        return (min_tree[idx], max_tree[idx])
    
    mid = (start + end) // 2
    left_child = init(idx * 2, start, mid)
    right_child = init(idx * 2 + 1, mid + 1, end)
    min_tree[idx] = min(left_child[0], right_child[0])
    max_tree[idx] = max(left_child[1], right_child[1])
    return (min_tree[idx], max_tree[idx])


def find(idx, start, end, left, right):
    if start > right or end < left:
        return (INF, 1)
    if left <= start and right >= end:
        return (min_tree[idx], max_tree[idx])
    
    mid = (start + end) // 2
    left_child = find(idx * 2, start, mid, left, right)
    right_child = find(idx * 2 + 1, mid + 1, end, left, right)
    return (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))


init(1, 1, N)
for _ in range(M):
    a, b = map(int, input().split())
    print(*find(1, 1, N, a, b))
