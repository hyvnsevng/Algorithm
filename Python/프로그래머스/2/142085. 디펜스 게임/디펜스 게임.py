from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    mjk = []
    sum_hq = 0
    used_army = 0
    for i in range(len(enemy)):
        heappush(mjk, enemy[i])
        sum_hq += enemy[i]
        if len(mjk) > k:
            x = heappop(mjk)
            sum_hq -= x
        used_army += enemy[i]
        if n < used_army - sum_hq:
            break
        answer += 1
        
    return answer
