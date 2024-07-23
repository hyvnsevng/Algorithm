import sys

N = int(input())
length = list(map(int, sys.stdin.readline().split()))

cost_list = list(map(int, sys.stdin.readline().split()))


cheapest_cost = cost_list[0]
total_cost = 0
index = 0

for i in range(1, N):
    if cost_list[i] < cheapest_cost:
        
        total_cost += cheapest_cost*(sum(length[index:i]))
        index = i
        cheapest_cost = cost_list[i]
else:
    total_cost += cheapest_cost*(sum(length[cost_list.index(cheapest_cost):]))
        
print(total_cost)