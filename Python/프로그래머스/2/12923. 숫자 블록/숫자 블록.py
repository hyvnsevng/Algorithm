def solution(begin, end):
    # {0, 1, 1, ...} 로 초기화(맨 앞이 0인 경우는 begin == 1인 경우, 그 외 모두 1)
    answer = [0 if begin == 1 else 1] + [1] * (end - begin)
    LIMIT = 10000000
        
    # 2부터 sqrt(end)까지 인수(i)를 늘려가면서 각 위치의 블록 확인
    # begin 이상의 i의 배수 탐색 -> i로 나눈 몫(블럭 숫자)으로 최대값 갱신
    # 만약 몫이 LIMIT보다 크다면 인수로 대체
    for i in range(2, int(end ** 0.5) + 1):                         # i: 인수
        for j in range(((begin + i - 1) // i) * i, end + 1, i):     # j: 블럭의 위치
            block = j // i if j // i <= 10000000 else i
            answer[j - begin] = max(answer[j - begin], block)
            
    return answer