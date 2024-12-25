n, m, b = map(int, input().split())

yard = []
max_h, min_h = 0, 1e9
sum_h = 0
# dif = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    max_tmp = max(tmp)
    min_tmp = min(tmp)
    if max_h < max_tmp:
        max_h = max_tmp
    if min_h > min_tmp:
        min_h = min_tmp
    sum_h += sum(tmp)
    yard.append(tmp)

# while True:
max_block = int(sum_h + b / (n*m))
# print(max_block)
ans = [1e9, 0]
for h in range(max_block, -1, -1):
    tmp = 0
    for i in range(n):
        for j in range(m):
            tmp_h = yard[i][j]
            if tmp_h > h:
                tmp += 2*(tmp_h - h)
            elif tmp_h < h:
                tmp += (h - tmp_h)
    if tmp < ans[0]:
        ans = [tmp, h]
    elif tmp == ans[0] and h > ans[1]:
        ans[1] = h

print(ans[0], ans[1])
# for i in range(n):
#     for j in range(m):
#         if


# print(max_h, min_h)


'''
1 32 2 24



'''