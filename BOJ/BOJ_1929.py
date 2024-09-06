# 백준 1929번 소수 구하기

m, n = map(int, input().split())
che = [0 for _ in range(n+1)]
nums = []
for i in range(2, n+1):
    if che[i] == 0:
        for j in range(i, n+1, i):
            che[j] = 1
        if i >= m:
            nums.append(i)
for num in nums:
    print(num)