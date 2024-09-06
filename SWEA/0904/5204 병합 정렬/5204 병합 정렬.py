def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    global ans

    result = []
    li, ri = 0, 0

    if left[-1] > right[-1]:
        ans += 1

    while li < len(left) or ri < len(right):
        if li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        elif li == len(left):
            result += right[ri:]
            break
        elif ri == len(right):
            result += left[li:]
            break

    return result


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    L = list(map(int, input().split()))
    ans = 0
    L = merge_sort(L)
    print(f'#{tc} {L[n//2]} {ans}')
