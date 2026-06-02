from itertools import combinations

def sys_res(comb, query):
    res = 0
    query_set = set(query)
    for num in comb:
        if num in query_set:
            res += 1
    return res


def backtracking(comb, q, ans, idx):
    if idx == len(ans):
        return 1
    if sys_res(comb, q[idx]) != ans[idx]:
        return 0
    return backtracking(comb, q, ans, idx + 1)

    
def solution(n, q, ans):
    answer = 0    
    for comb in combinations([x for x in range(1, n + 1)], 5):
        answer += backtracking(comb, q, ans, 0)
    return answer
