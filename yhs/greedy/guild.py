N = int(input())

guild = list(map(int, input().split()))


# 오름차순으로 정렬

for i in range(N-1):
    for j in range(N-1-i):
        if guild[j] > guild[j+1]:
            val = guild[j+1]
            guild[j+1] = guild[j]
            guild[j] = val
# print(guild)


# 그리디(공포도 작은 순서로 그룹 묶기)

num_of_group = 0
group_size = 1

for fear in guild:
    if fear <= group_size:      # 현재까지 모인 그룹 인원수가 그룹 내 최대 공포도보다 많아졌을 때 -> 그룹 생성 
        group_size = 1
        num_of_group += 1
        # print(f'{fear}명 그룹 추가')
        continue

    group_size += 1

print(num_of_group)