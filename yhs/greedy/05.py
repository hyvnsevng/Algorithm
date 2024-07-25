N, M = map(int, input().split())

weight_list = list(map(int, input().split()))

count_num = []

for i in range(1, M+1):
    count_num.append(weight_list.count(i))
    
ans = 0

for i in range(len(count_num)-1):
    ans += count_num[i]*sum(count_num[i+1:])

print(ans)