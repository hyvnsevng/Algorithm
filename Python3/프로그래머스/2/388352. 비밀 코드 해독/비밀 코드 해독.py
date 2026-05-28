from itertools import combinations

def solution(n, q, ans):
    codes = list(combinations(range(1, n + 1), 5))

    for query, cnt in zip(q, ans):
         codes = [code for code in codes if len(set(code) & set(query)) == cnt]

    return len(codes)