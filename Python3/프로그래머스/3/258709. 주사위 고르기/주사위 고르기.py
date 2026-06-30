from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    half = n // 2
    
    max_win = 0
    answer = []

    # A가 가져간 주사위 조합
    for a_indices in combinations(range(n), half):
        a_set = set(a_indices)
        b_indices = [i for i in range(n) if i not in a_set]

        # 현재 조합에서 A, B가 얻을 수 있는 모든 점수의 경우
        a_sums = []
        b_sums = []

        for faces in product(range(6), repeat=half):
            a_sums.append(sum(dice[idx][face] for idx, face in zip(a_indices, faces)))
            b_sums.append(sum(dice[idx][face] for idx, face in zip(b_indices, faces)))

        b_sums.sort()

        win_count = 0
        for a_sum in a_sums:
            # b_sums 중 a_sum보다 작은 값의 개수 (A가 이기는 경우의 수)
            win_count += bisect_left(b_sums, a_sum)

        if win_count > max_win:
            max_win = win_count
            answer = [idx + 1 for idx in a_indices]

    return answer