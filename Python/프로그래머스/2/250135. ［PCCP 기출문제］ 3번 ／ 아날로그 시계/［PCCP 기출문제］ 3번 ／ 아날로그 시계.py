def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    st = h1 * 3600 + m1 * 60 + s1   # 시작 시간
    et = h2 * 3600 + m2 * 60 + s2   # 종료 시간
    
    for h in range(h1, h2 + 1):
        for m in range(m1 if h1 == h else  0, m2 + 1 if h2 == h else 60):
            hs = ((h % 12) * 3600 + 60 * m) / 719   # 시침과 초침이 겹침
            ms = (60 * m) / 59                      # 분침과 초침이 겹침
            hm = h * 3600 + m * 60                  # h시 m분을 초 단위로 변환
            
            # 시침과 초침이 겹치는 시간이 범위 안에 존재
            if st <= hm + hs <= et and 0 <= hs < 60:
                answer += 1
            # 분침과 초침이 겹치는 시간이 범위 안에 존재
            if st <= hm + ms <= et and 0 <= ms < 60:
                answer += 1
    
    # 시침+분침+초침이 모두 겹치는 시간: 0시 0분 0초, 12시 0분 0초
    hms = (0, 12 * 3600)
    for t in hms:
        if st <= t <= et:
            answer -= 1
            
    return answer
