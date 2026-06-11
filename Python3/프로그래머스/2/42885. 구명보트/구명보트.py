def solution(people, limit):
    n = len(people)
    answer = n
    people.sort()
    s, e = 0, n - 1
    while s < e:
        if people[s] + people[e] <= limit:
            answer -= 1
            s += 1
        e -= 1
    return answer
