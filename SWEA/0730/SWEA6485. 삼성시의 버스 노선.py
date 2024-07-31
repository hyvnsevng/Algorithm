import sys

sys.stdin = open('s_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    # 버스 노선 개수
    N = int(input())

    # 노선 정보(리스트로 저장)
    bus_line = []
    for _ in range(N):
        mylist = list(map(int, input().split()))
        bus_line.append(mylist)

    # 버스정류장
    P = int(input())
    bus_check = []
    for _ in range(P):
        temp = int(input())
        bus_check.append(temp)

    # bus_check에 포함된 버스 정류장 지나는 지 확인
    ans = [0 for i in range(len(bus_check))]    # C1, C2, C3,...을 지나는 버스 개수

    for i in range(len(bus_check)):
        for line in bus_line:
            if line[0]<=bus_check[i]<=line[1]:
                ans[i] += 1

    print(f'#{tc} ', end='')
    for _ in ans:
        print(_, end=' ')
    print()