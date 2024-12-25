'''
백준 18111번 마인크래프트

1. 땅의 높이를 2차원 배열에 저장하면서 최대 높이, 최소 높이, 높이의 합을 구한다.
2. 인벤토리에 있는 블록과 높이의 합을 더한 값을 집터의 넓이로 나누어, 땅을 고른 결과 될 수 있는 최대 높이(max_block)을 구한다.
3. 만약 max_block이 최대 높이보다 크다면, 최대높이 + 1부터, 아니라면 max_block부터 0까지 1씩 줄여가며 반복 시작.
3-1. 해당 높이로 땅을 고르기 위한 시간, 땅의 높이를 구한다.
3-2. 만약 더 적은 시간이 소요된다면 시간과 높이를 갱신, 같은 시간이 소요되고 높이가 더 높다면 높이 갱신
3-3. 답을 출력한다.

- Python3로 풀 경우 시간초과, PyPy3로 풀 경우 통과하였다.
- Python3로도 통과할 수 있도록 시간복잡도를 고려해 다른 풀이를 생각해보자.
'''

n, m, b = map(int, input().split())

yard = []
max_h, min_h = 0, 1e9
sum_h = 0

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

max_block = int((sum_h + b) /   (n*m))
ans = [1e9, 0]
if max_block > max_h:
    start = max_h + 1
else:
    start = max_block

# print(max_block, max_h, start)
for h in range(start, -1, -1):
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