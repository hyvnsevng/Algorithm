numbers = list(map(int, input()))

ans = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < 2 or ans < 2:       # 계산식에 0 혹은 1 포함 시 더하기 연산
        ans += numbers[i]
    else:                               # 그 외 곱하기 연산
        ans *= numbers[i]

print(ans)
