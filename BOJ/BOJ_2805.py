# 백준 2805번 나무 자르기

# PyPy로만 통과...
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start, end = trees[-1] - m, trees[-1] - 1

while start <= end:
    mid = (end + start) // 2
    total_len = 0
    for i in range(len(trees)-1, -1, -1):
        len_tree = trees[i]
        if len_tree - mid < 0:
            break
        total_len += len_tree - mid
    # print(start, end, mid, total_len)
    if total_len < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)

# # Python3 코드
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))
#
# start, end = 0, max(trees)
#
# while start <= end:
#     mid = (end + start) // 2
#     total_len = 0
#     for tree in trees:
#         if tree - mid >= 0:
#             total_len += tree - mid
#     # print(start, end, mid, total_len)
#     if total_len >= m:
#
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)