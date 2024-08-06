import sys

sys.stdin = open('sample_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    t, p = map(str, input().split())

    n = len(t)
    m = len(p)
    i = 0
    answer = 0

    while i < n:
        # 패턴 전체가 문자열에 있는지 확인
        if i + m - 1 < n:
            for j in range(0, m):
                if p[j] != t[i+j]:  # 다를 시 즉시 다음 인덱스로 넘어가고 반복 탈출
                    if not j:
                        i += j+1
                        answer += j+1
                    else:
                        i += j
                        answer += j
                    break
            else:
                i += m
                answer += 1
                # 첫글자 일치하지 않을 시 다음 인덱스 확인
            continue
        answer += n-i
        i = n

    print(f'#{tc} {answer}')