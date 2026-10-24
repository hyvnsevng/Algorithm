def solution(begin, end):
    # {0, 1, 1, ...} 로 초기화(맨 앞이 0인 경우는 begin == 1인 경우, 그 외 모두 1)
    # 2부터 sqrt(end)까지 인수를 늘려가면서 각 위치의 블록 확인
    # 인수로 나눠 떨어지는 경우 나눈 몫으로 대체(최초 1회)
    answer = [0 if begin == 1 else 1] + [1] * (end - begin)
        
    for i in range(2, int(end ** 0.5) + 1):                         # i: 인수
        for j in range(((begin + i - 1) // i) * i, end + 1, i):     # j: 블럭의 위치
            idx = j - begin
            # 블럭 숫자가 10,000,000보다 큰 경우: 인수로 대체
            if j // i > 10000000:
                answer[idx] = max(i, answer[idx])
            if i != j and j // i <= 10000000:
                answer[idx] = max(j // i, answer[idx])
            
    return answer