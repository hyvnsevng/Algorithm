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
nums = list(map(int, input().split()))
lis = [nums[0]]

for num in nums:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = binary_search(lis, num)
        lis[idx] = num

print(len(lis))