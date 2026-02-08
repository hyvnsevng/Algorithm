n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

locations = [1000001 for _ in range(max_num +1)]
for i in range(n):
    locations[arr[i]] = i

nums = set(arr)
score = [0 for _ in range(n)]

gcd = [[] for _ in range(max_num + 1)]
for i in sorted(nums):
    k = 2*i
    while k <= max_num:
        gcd[k].append(i)
        k += i
    
for i in range(n):
    card = arr[i]
    for num in gcd[card]:
        if num in nums:
            score[locations[num]] += 1
            score[i] -= 1 

print(*score)