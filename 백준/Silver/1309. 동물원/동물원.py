import sys
input = sys.stdin.readline

MOD = 9901
n = int(input())
left, right, no = 1, 1, 1
for i in range(1, n):
    left, right, no = (right + no) % MOD, (left + no) % MOD, (left + right + no) % MOD

print((left + right + no)%MOD)
