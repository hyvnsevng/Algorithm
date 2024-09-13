# 백준 11723번 집합
import sys
input = sys.stdin.readline

S = set()
n = int(input())
for _ in range(n):
    string = input()
    if 'all' in string:
        S = set([i for i in range(1, 21)])
    elif 'empty' in string:
        S = set()
    else:
        do, num = string.split()
        num = int(num)
        if do == 'add':
            S.add(num)
        elif do == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif do == 'remove':
            if num in S:
                S.remove(num)
        elif do == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
