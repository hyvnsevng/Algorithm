def segment(left, right, i=1):
    if left == right:
        tree[i] = nums[left]
        return tree[i]
    mid = (left + right) // 2
    tree[i] = (segment(left, mid, i * 2) * segment(mid + 1, right, i * 2 + 1)) % 1000000007
    return tree[i]


def update(start, end, idx, diff, i=1):

    while start != end:
        mid = (start + end) // 2
        if idx <= mid:
            i *= 2
            end = mid
        elif idx > mid:
            i = i * 2 + 1
            start = mid + 1

    tree[i] = diff
    i //= 2
    while i > 0:
        tree[i] = (tree[i*2] * tree[i*2+1]) % 1000000007
        i //= 2
    #
    # if idx < start or idx > end:
    #     return
    #
    # tree[i] *= (diff / nums[idx])
    # if start == end:
    #     return
    #
    # mid = (start + end) // 2
    #
    # update(start, mid, idx, diff, i * 2)
    # update(mid + 1, end, idx, diff, i * 2 + 1)


def multiple(start, end, left, right, i=1):
    if end < left or start > right:
        return 1

    if start >= left and end <= right:
        return tree[i]

    mid = (start + end) // 2

    return (multiple(start, mid, left, right, i * 2) * multiple(mid + 1, end, left, right, i * 2 + 1)) % 1000000007


n, m, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

tree = [0] * (4*len(nums))
segment(0, len(nums) - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, len(nums) - 1, b - 1, c)
    elif a == 2:
        print(int(multiple(0, len(nums) - 1, b-1, c-1)))
