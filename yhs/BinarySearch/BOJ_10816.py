from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
lst = list(map(int, input().split()))
ans = [0] * m

for i in range(m):
    a, b = bisect_left(cards, lst[i]), bisect_right(cards, lst[i])
    print(b-a, end = ' ')