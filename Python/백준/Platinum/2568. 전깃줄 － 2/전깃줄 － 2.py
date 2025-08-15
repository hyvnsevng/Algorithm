def binary_search(arr, target):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return s

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines.sort()

v = [lines[0][1]]
backtrace = []

for line in lines:
    if v[-1] < line[1]:
        v.append(line[1])
        backtrace.append((len(v) - 1, line))
    else:
        idx = binary_search(v, line[1])
        v[idx] = line[1]
        backtrace.append((idx, line))

idx = len(v) - 1
ans = []
while backtrace:
    i, line = backtrace.pop()

    if idx < 0:
        ans.append(line[0])
        continue

    if idx == i:
        idx -= 1
    else:
        ans.append(line[0])

print(len(ans))
for elem in ans[::-1]:
    print(elem)
