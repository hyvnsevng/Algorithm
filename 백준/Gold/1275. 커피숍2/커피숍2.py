import sys

input = sys.stdin.readline

n, q = map(int, input().split())
nums = list(map(int, input().split()))

tree = [0] * (4*n)


def init(node=0, start=0, end=n-1):
    if start >= end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2 + 1, start, mid) + init(node * 2 + 2, mid+1, end)
    return tree[node]


def get(left, right, start=0, end=n-1, node=0):
    if left > end or right < start:
        return 0
    if left <= start  and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return get(left, right, start, mid, node * 2 + 1) + get(left, right, mid+1, end, node * 2 + 2)


def update(idx, val, start=0, end=n-1, node=0):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] += (val - nums[idx])
        nums[idx] = val
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = update(idx, val, start, mid, node * 2 + 1) + update(idx, val, mid+1, end, node*2+2)
    return tree[node]


init()      # 트리 생성

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(get(x-1, y-1))    # x, y 구간합 출력
    update(a-1, b)    # a번째 수를 b로 변경
