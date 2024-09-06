# 백준 11866번 요세푸스 문제 0

n, k = map(int, input().split())

nums = [i for i in range(1, n+1)]
joseph = []

idx = k-1
size = n

while len(joseph) < n-1:
    num = nums[idx]
    joseph.append(num)
    nums.remove(num)

    size = len(nums)
    idx = (idx - 1 + k) % size

print('<', end ='')
for i in joseph:
    print(i, end = ', ')
print(f'{nums[0]}>')
