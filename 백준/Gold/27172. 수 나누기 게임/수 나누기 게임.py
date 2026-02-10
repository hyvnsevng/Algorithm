n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

locations = dict()
for i in range(n):
    locations[arr[i]] = i

score = [0 for _ in range(n)]

for i in arr:
    k = 2*i
    while k <= max_num:
        find = locations.get(k, -1)
        if find >= 0:
            score[find] -= 1
            score[locations[i]] += 1 
        k += i

print(*score)