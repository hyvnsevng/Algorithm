# 백준 9375번 패션왕 신해빈

# 의상의 종류와 이름이 주어졌을 때, 같은 종류의 의상은 하나만 입을 수 있고 매일 다른 조합으로 의상을 입어야 한다면
# 해빈이는 최대 며칠을 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을지 구하는 문제

# (종류 별 옷의 개수 + 1(입지 않는 경우))을 모두 곱한 것에서 1을 뺀 것(아무 옷도 입지 않는 경우)이 정답이다.

import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    n = int(input())
    acc_dict = dict()
    acc_set = set()
    for i in range(n):
        value, key = input().split()
        tmp = acc_dict.get(key, 0)
        acc_dict[key] = tmp + 1
    ans = 1
    for key in acc_dict:
        ans *= (acc_dict[key]+1)
    print(ans-1)