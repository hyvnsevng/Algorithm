# import sys
# sys.setrecursionlimit(10**7)

def merge_sort(lst):  # A[p..r]을 오름차순 정렬한다.
    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2 + 0.5)   # 문제에서 요구하는 중간 : 홀수번째면 반올림한 값
    left = lst[:mid]
    right = lst[mid:]

    merged_left = merge_sort(left)
    # if not merged_left:
    #     return
    merged_right = merge_sort(right)
    # if not merged_right:
    #     return
    merged = merge(merged_left, merged_right)
    # if not merged:
    #     return

    return merged


def merge(left, right):
    # print(left, right)
    global k

    i, j = 0, 0
    tmp = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            # print(left[i])
            k -= 1
            if not k:
                print(left[i])
                # return
            i += 1          # tmp[t] <- A[i]; t++; i++;
        else:
            tmp.append(right[j])
            # print(right[j])
            k -= 1
            if not k:
                print(right[j])
                # return
            j += 1          # tmp[t] <- A[j]; t++; j++;

    while i < len(left):
        tmp.append(left[i])
        # print(left[i])
        k -= 1
        if not k:
            print(left[i])
            # return
        i += 1
    while j < len(right):
        tmp.append(right[j])
        # print(right[j])
        k -= 1
        if not k:
            print(right[j])
            # return
        j += 1

    return tmp


n, k = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(A)
if k > 0:
    print(-1)