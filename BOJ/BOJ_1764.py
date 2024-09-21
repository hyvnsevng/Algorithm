# 백준 1764번 듣보잡

n, m = map(int, input().split())
heard = set(list(input() for _ in range(n)))
seen = set(list(input() for _ in range(m)))
dbj = sorted(heard & seen)
print(len(dbj))
for item in dbj:
    print(item)