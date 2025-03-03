n = int(input())
numList = list(map(int, input().split()))
v = numList[0:1]
backtrace = list()

for num in numList:
    if v[-1] < num:
        v.append(num)
        backtrace.append((len(v) - 1, num))
    else:
        start, end = 0, len(v)-1
        while start < end:
            mid = (start + end) // 2
            if v[(start + end) // 2] < num:
                start = mid + 1
            else:
                end = mid

        v[end] = num
        backtrace.append((end, num))

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