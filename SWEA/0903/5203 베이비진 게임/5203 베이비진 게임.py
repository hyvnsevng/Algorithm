import sys

sys.stdin = open('5203_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1, player2 = [0 for _ in range(10)], [0 for _ in range(10)]

    win = 0

    for i in range(len(cards)//2):
        player1[cards[i*2]] += 1
        player2[cards[i * 2 + 1]] += 1

        print(player1, player2)

        run1, run2 = 0, 0

        if i >= 2:
            for j in range(10):
                if player1[j]:
                    run1 += 1
                else:
                    run1 = 0

                if run1 > 2:
                    win = 1
                    break

                if player1[j] > 2:
                    win = 1
                    break

                if player2[j]:
                    run2 += 1
                else:
                    run2 = 0

                if run2 > 2:
                    win = 2
                    break
                if player2[j] > 2:
                    win = 2
                    break

        if win:
            break

    print(f'#{tc} {win}')


