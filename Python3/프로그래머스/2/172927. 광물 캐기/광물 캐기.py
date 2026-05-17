idx_dict = dict()
idx_dict["diamond"] = 0
idx_dict["iron"] = 1
idx_dict["stone"] = 2

'''
몇번째 광물인지, 곡괭이 개수, 피로도, 현재 곡괭이
'''
def dfs(idx, acc, res, picks, minerals):
    if idx >= len(minerals):
        return acc
    
    pick_cnt = 0
    for pick in range(3):
        if picks[pick] == 0:
            pick_cnt += 1
            continue
        t_pick = [p for p in picks]
        t_pick[pick] -= 1
        tmp = acc
        for i in range(idx, min(idx+5, len(minerals))):
            mineral = idx_dict[minerals[i]]
            diff = pick - mineral
            if diff == 2:
                tmp += 25
            elif diff == 1:
                tmp += 5
            else:
                tmp += 1
                
        if pick == 0:
            res = min(res, dfs(idx+5, tmp, res, t_pick, minerals))
        elif pick == 1:
            res = min(res, dfs(idx+5, tmp, res, t_pick, minerals))
        else:
            res = min(res, dfs(idx+5, tmp, res, t_pick, minerals))
    
    if pick_cnt == 3:
        return acc
    return res


def solution(picks, minerals):
    answer = dfs(0, 0, 25*51, picks, minerals)
    
    
    
        
    
    
    return answer

