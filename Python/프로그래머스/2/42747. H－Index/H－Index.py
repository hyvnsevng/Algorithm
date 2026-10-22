def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    for i in range(n):
        # i번째 값이 c -> c번 이상 인용된 논문이 i + 1편 이상
        answer = max(min(i + 1, citations[i]), answer)
            
    return answer