n = int(input())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

answer = []

# 1번 쿼리: 모든 홀수
for v in range(1, n + 1, 2):
    answer.append((1, v))

# 2번 쿼리: 모든 합성수
for v in range(2, n + 1):
    if not is_prime[v]:
        answer.append((2, v))

print(len(answer))
for q, v in answer:
    print(q, v)
