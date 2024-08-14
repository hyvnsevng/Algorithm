import sys

sys.stdin = open('sample_in.txt')


def pack(arr):
    total = sum(arr)
    length = len(arr)
    min_diff = 1000

    for i in range(1, length-1):
        for j in range(i+1, length):
            packed = [sum(arr[:i]), sum(arr[i:j]), sum(arr[j:])]
            for count in packed:
                if count > total//2:
                    break
            else:
                diff = max(packed) - min(packed)
                if diff < min_diff:
                    min_diff = diff

    if min_diff == 1000:
        return -1
    else:
        return (min_diff)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())        # 당근의 개수
    carrots = list(map(int, input().split()))
    carrots.sort()

    num_carrots = [0 for _ in range(carrots[-1])]

    for carrot in carrots:
        num_carrots[carrot-1] += 1

    print(f'#{tc} {pack(num_carrots)}')
