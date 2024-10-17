# 백준 2503번 숫자 야구

from itertools import permutations

n = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cases = set(permutations(nums, 3))

for _ in range(n):
    game, strike, ball = map(int, input().split())
    given = list(map(int, str(game)))

    byebye = []

    for case in cases:
        strike_, ball_ = 0, 0
        for i in range(3):
            if given[i] == case[i]:
                strike_ += 1
            if case[i] in given and given[i] != case[i]:
                ball_ += 1

        if not (strike_ == strike and ball_ == ball):
            byebye.append(case)

    for bye in byebye:
        cases.remove(bye)

print(len(cases))