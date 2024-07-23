N, K = map(int, input().split())

coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

num_of_coins = 0

for coin in coin_list:
    if K >= coin:
        num_of_coins += (K//coin)
        K %= coin


print(num_of_coins)
