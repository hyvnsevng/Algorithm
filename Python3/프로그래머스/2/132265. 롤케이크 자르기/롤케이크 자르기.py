def solution(topping):
    answer = 0
    n = len(topping)
    counts = dict()
    for i in range(n):
        key = topping[i]
        counts[key] = counts.get(key, 0) + 1
        
    entire = set(topping)
    cheolsoo = set()
    for i in range(n):
        curr = topping[i]
        cheolsoo.add(curr)
        counts[curr] -= 1
        if counts[curr] == 0:
            entire.remove(curr)
        if len(cheolsoo) == len(entire):
            answer += 1
    return answer