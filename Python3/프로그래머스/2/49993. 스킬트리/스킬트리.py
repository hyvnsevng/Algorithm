def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    skill_order = [0] * 27
    BASE = 64
    for i in range(len(skill) - 1):
        _prev = ord(skill[i]) - BASE
        _next = ord(skill[i + 1]) - BASE
        skill_order[_next] = _prev
        
    for skill_tree in skill_trees:
        learned = [False] * 27
        learned[0] = True
        for s in skill_tree:
            skill_num = ord(s) - BASE
            prelearned = skill_order[skill_num]
            if not learned[prelearned]:
                break
            learned[skill_num] = True
        else:
            answer += 1
            
    return answer