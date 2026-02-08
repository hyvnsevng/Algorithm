n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

locations = [1000001 for _ in range(1000001)]
for i in range(n):
    locations[arr[i]] = i

score = [0 for _ in range(n)]

for i in arr:
    k = 2*i
    while k <= max_num:
        find = locations[k]
        if find < 1000001:
            score[find] -= 1
            score[locations[i]] += 1 
        k += i

print(" ".join(map(str, score)))