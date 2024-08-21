n = int(input())
warehouse = [list(map(int, input().split())) for _ in range(n)]
where_is_max = sorted(warehouse, key=lambda x: -x[1])
max_info = where_is_max[0]
warehouse.sort()

area = 0
stack = []

for i in range(n):
    if stack:
        prev = stack.pop()
        area += prev[1] * (warehouse[i][0] - prev[0])
        if prev[1] > warehouse[i][1]:
            stack.append([warehouse[i][0], prev[1]])
        else:
            stack.append(warehouse[i])
    else:
        stack.append(warehouse[i])

    if warehouse[i] == max_info:
        area += max_info[1]
        break

stack = []

for i in range(n-1, -1, -1):
    if stack:
        prev = stack.pop()
        area += prev[1] * (prev[0] - warehouse[i][0])
        if prev[1] > warehouse[i][1]:
            stack.append([warehouse[i][0], prev[1]])
        else:
            stack.append(warehouse[i])
    else:
        stack.append(warehouse[i])

    if warehouse[i] == max_info:
        break

print(area)

'''
5
1 5
2 4
3 2
4 3
5 1'''