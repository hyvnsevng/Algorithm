def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    for i in range(n):
        # i번째 값이 c -> c번 이상 인용된 논문이 i + 1편 이상이어야 함
        c = citations[i]
        
        if c < i + 1:
            return i
            
    return n