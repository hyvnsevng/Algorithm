n, m = map(int, input().split())
password = dict()
for _ in range(n):
    key, val = input().split()
    password[key] = val

for _ in range(m):
    key = input()
    print(password[key])
