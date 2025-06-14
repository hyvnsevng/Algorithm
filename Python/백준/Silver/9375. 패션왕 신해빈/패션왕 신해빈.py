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