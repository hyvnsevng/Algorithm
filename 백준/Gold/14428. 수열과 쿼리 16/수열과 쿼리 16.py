import sys
input = sys.stdin.readline
# input = open('input.txt', 'r').readline

INF = 10e9

N = int(input())
arr = [INF] + list(map(int, input().split()))
st = [0] * (4 * N + 1)


def init(idx, start, end):
    if start == end:
        st[idx] = (arr[start], start)
        return st[idx]
    mid = (start + end) // 2
    left_child, right_child = init(idx * 2, start, mid), init(idx * 2 + 1, mid + 1, end)
    st[idx] = min(left_child, right_child)
    return st[idx]


def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        st[node] = (val, idx)
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)
    st[node] = min(st[node * 2], st[node * 2 + 1])


def get(idx, start, end, left, right):
    if start > right or end < left:
        return (INF, 0)
    if left <= start and end <= right: return st[idx]

    mid = (start + end) // 2
    left_child, right_child = get(idx * 2, start, mid, left, right), get(idx * 2 + 1, mid + 1, end, left, right)
    return min(left_child, right_child)
    

init(1, 1, N)
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
        update(1, 1, N, b, c)
    elif a == 2:
        print(get(1, 1, N, b, c)[1])
