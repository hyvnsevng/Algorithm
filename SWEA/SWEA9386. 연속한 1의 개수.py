import sys

sys.stdin = open('input1.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))

    cnt = 0
    maxcnt = 0

    # 리스트 순회
    for num in nums:
        if num:
            cnt += 1
            # 최대 연속 횟수 갱신
            if cnt > maxcnt:
                maxcnt = cnt

        # 연속 끊길 시 cnt 초기화
        else:
            cnt = 0


    print(f'#{tc} {maxcnt}')