import sys
from collections import deque

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))

    queue = deque()

    for price in prices:
        if


