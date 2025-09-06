import sys
input = sys.stdin.readline

R, C = map(int, input().split())
# 보드를 비트로 전처리 (대문자 기준: 'A'->0)
board = [[1 << (ord(ch) - 65) for ch in input().strip()] for _ in range(R)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

best = 1
start_mask = board[0][0]

# 스택: (r, c, mask, depth)
stack = [(0, 0, start_mask, 1)]

# ---- 선택적 가지치기(권장) ----
# 같은 (r,c,mask)로 더 얕은/같은 깊이로 오면 이득 없음 → 스킵
# 메모리 과다해질 정도는 아님(경로 수가 제한적)
seen_depth = {(0, 0, start_mask): 1}
# --------------------------------

while stack:
    r, c, mask, depth = stack.pop()
    if depth > best:
        best = depth
        if best == 26:     # 알파벳 최대치 도달 시 즉시 종료
            break

    # 로컬 바인딩으로 미세 최적화
    m = mask
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            bit = board[nr][nc]
            if (m & bit) == 0:
                nm = m | bit
                nd = depth + 1
                # 가지치기: 같은 상태를 더 짧게 온 적 있으면 스킵
                key = (nr, nc, nm)
                if seen_depth.get(key, 0) >= nd:
                    continue
                seen_depth[key] = nd
                stack.append((nr, nc, nm, nd))

print(best)
