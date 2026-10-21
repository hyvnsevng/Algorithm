def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    st = h1 * 3600 + m1 * 60 + s1
    et = h2 * 3600 + m2 * 60 + s2
    time_set = set()
    for h in range(h1, h2 + 1):
        for m in range(m1 if h1 == h else  0, m2 + 1 if h2 == h else 60):
            hs = ((h % 12) * 3600 + 60 * m) / 719
            ms = (60 * m) / 59
            hm = h * 3600 + m * 60
            if st <= hm + hs <= et and 0 <= hs < 60:
                time_set.add(hm + hs)
            if st <= hm + ms <= et and 0 <= ms < 60:
                time_set.add(hm + ms)
                
    return len(time_set)
