import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    if k < 5:
        print(0)
        return

    # 단어들을 비트마스크로 변환
    words_bit = []
    for _ in range(n):
        bit = 0
        for char in input().strip():
            bit |= (1 << (ord(char) - ord('a')))
        words_bit.append(bit)

    # 기본 필수 글자 (acint)
    base_mask = 0
    for c in "acint":
        base_mask |= (1 << (ord(c) - ord('a')))

    # 후보 글자들
    candidates = [i for i in range(26) if not (base_mask & (1 << i))]

    def dfs(idx, count, current_mask):
        if count == k - 5:
            read_cnt = 0
            for w_bit in words_bit:
                if (w_bit & current_mask) == w_bit:
                    read_cnt += 1
            return read_cnt

        res = 0
        for i in range(idx, len(candidates)):
            # 최댓값 갱신
            res = max(res, dfs(i + 1, count + 1, current_mask | (1 << candidates[i])))
        return res

    print(dfs(0, 0, base_mask))

solve()