S = list(map(int, input()))

zeros = 0           # 0으로 묶인 횟수
ones = 0            # 1로 묶인 횟수
last_num = S[0]     # last_num : 마지막으로 묶인 숫자


if last_num == 0:       # 문자열의 첫 묶음
    zeros +=1
else:
    ones += 1


# 문자열에서 0, 1 숫자 그룹 세기
for number in S:                    # (0과 1로만 구성되어 있으므로 대소로 판별 가능)
    if number < last_num:
        last_num = number
        zeros += 1
    elif number > last_num:
        last_num = number
        ones += 1
    

# 0, 1 그룹 중 작은 수 출력
if zeros > ones:
    print(ones)
else:
    print(zeros)
