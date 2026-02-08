n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

locations = [1000001 for _ in range(max_num +1)]
for i in range(n):
    locations[arr[i]] = i

arr.sort()

nums = set(arr)
score = [0 for _ in range(n)]

gcd = [[] for _ in range(max_num + 1)]
for i in arr:
    k = 2*i
    while k <= max_num:
        if k in nums:
            score[locations[k]] -= 1
            score[locations[i]] += 1 
        k += i

print(*score)