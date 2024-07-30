def find_max(arr):

    # 리스트 내 최대값과 그 인덱스 찾기 (뒤에서부터)

    temp = arr[-1]
    idx = len(arr)-1
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > temp:
            temp = arr[i]
            idx = i

    return idx, temp

import sys

sys.stdin = open('4834_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    a = list(map(int, input()))

    garbage, max_val = find_max(a)      # garbage: 버리는 값, max_val: 숫자 중 최대값

    mylist = [0 for _ in range(max_val+1)]

    for num in a:
        mylist[num] += 1                # mylist의 인덱스가 a에 등장한 횟수

    ans1, ans2 = find_max(mylist)

    print(f'#{tc} {ans1} {ans2}')

