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
numList = list(map(int, input().split()))
v = numList[0:1]
backtrace = list()

for num in numList:
    if v[-1] < num:
        v.append(num)
        backtrace.append((len(v) - 1, num))
    else:
        idx = binary_search(v, num)
        v[idx] = num
        backtrace.append((idx, num))

idx = len(v) - 1

while backtrace:
    i, num = backtrace.pop()
    if idx == i:
        v[i] = num
        idx -= 1

    if idx < 0:
        break


print(len(v))
for elem in v:
    print(elem, end=" ")