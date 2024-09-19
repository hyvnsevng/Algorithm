import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0]*(n+1)
for i in range(n):
    sum_lst[i+1] = sum_lst[i]+lst[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(sum_lst[b]-sum_lst[a-1])