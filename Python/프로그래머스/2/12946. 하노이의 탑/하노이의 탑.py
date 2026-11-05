rep1 = {
    1: 1,
    2: 3,
    3: 2
}

rep2 = {
    1: 2,
    2: 1,
    3: 3
}

def solution(n):
    if n == 1:
        return [[1, 3]]
    prev = solution(n - 1)
    res = [[rep1[a], rep1[b]] for a, b in prev] + [[1, 3]] + [[rep2[a], rep2[b]] for a, b in prev]
    return res
