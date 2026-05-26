def solution(targets):
    answer = 0
    targets.sort()
    l, r = 100000000, -1
    for s, e in targets:
        if l <= s < r:
            l = max(l, s)
            r = min(r, e)
        else:
            answer += 1
            l , r = s, e
            
    return answer
