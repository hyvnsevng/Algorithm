N = int(input())
coins = list(map(int, input().split()))
coins.sort()

# sums = [0 for i in range(sum(coins))]

sum_coin = coins[0]


# 가장 작은 화폐단위가 2 이상일 경우
if coins[0] > 1:
    print(1)


else:
    for i in range(len(coins)-1):
        # 화폐단위가 연속된 정수일 경우
        if coins[i+1] - coins[i] <= 1:
            sum_coin += coins[i+1]
        else:
            # (~연속~ 까지의 합 + 1) 이 다음 동전보다 작을 경우 : 만들 수 없는 금액
            if coins[i+1] - sum_coin > 1:
                print(sum_coin+1)
                break
            else:
                sum_coin += coins[i+1]
    else:
        print(sum(coins)+1)
