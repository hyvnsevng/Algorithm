import sys
sys.stdin = open("sample_input.txt", "r")

for test_case in range(1, 11):
    N = int(input())        # 건물 수
    buildings = list(map(int, input().split()))     # 건물 높이

    sum_jomang = 0

    for i in range(2, N-2):
        jomang = 255                # 조망권확보세대수 초기화

        # 양옆 두 건물 확인
        for j in range(1, 3):
            if buildings[i]-buildings[i-j] < jomang:
                jomang = buildings[i]-buildings[i-j]
            if buildings[i] - buildings[i+j] < jomang:
                jomang = buildings[i] - buildings[i+j]

        # 조망권 확보(양수)한 경우에만 결과에 포함
        if jomang > 0:
            sum_jomang += jomang

    print(f'#{test_case} {sum_jomang}')
        # for j in range()
        # jomang[i-2]
