def count_sort(arr):                # counting sort
    max_val = find_max(arr)
    count = [0 for _ in range(max_val+1)]
    temp = [0 for _ in range(len(arr))]

    for num in arr:
        count[num] += 1

    for i in range(max_val):
        count[i+1] += count[i]

    for i in range(len(arr)-1, -1, -1):

        count[arr[i]] -= 1
        temp[count[arr[i]]] = arr[i]

    return temp


def find_max(arr):

    Mval = arr[0]

    for num in arr:
        if Mval<num:
            Mval = num

    return Mval


import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):

    dump = int(input())         # 덤프 횟수
    boxes = list(map(int, input().split()))         # 박스

    # 박스 오름차순 정렬
    boxes = count_sort(boxes)

    # 평탄화
    for _ in range(dump):
        # 최대-최소
        diff = boxes[-1]-boxes[0]

        # 평탄화 완료 시 결과 출력하고 반복문 탈출
        if diff < 2:
            print(f'#{tc} {diff}')
            break

        # 덤프 실행
        boxes[0] += 1
        boxes[-1] -= 1

        # 정렬
        boxes = count_sort(boxes)
    else:
        # 모든 덤프 시행 후 결과 출력
        print(f'#{tc} {boxes[-1] - boxes[0]}')





'''
평탄화 완료 시(최대-최소<=1) --> 높이 차 반환(0 or 1)
덤프 횟수
'''