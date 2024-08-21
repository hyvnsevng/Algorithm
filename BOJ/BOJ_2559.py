#  2559번 수열

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

start = 0
end = k
temp = sum(temperature[0:k])
max_sum = temp

for i in range(n-k):
    temp += (temperature[end] - temperature[start])
    if temp > max_sum:
        max_sum = temp

    start += 1
    end += 1

print(max_sum)