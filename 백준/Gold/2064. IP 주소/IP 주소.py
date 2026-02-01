import sys

input = sys.stdin.readline


def bit_to_ip(b):
    res = []
    for i in range(4):
        res.append(str(b >> (8 * (3-i)) & 255))
    return ".".join(res)


n = int(input())

minIP = (1 << 32) - 1
maxIP = 0
for _ in range(n):
    ip = list(map(int, input().split(".")))
    bits = 0
    for i in range(3, -1, -1):
        bits |= ip[i] << (24-i*8)
    if bits < minIP:
        minIP = bits
    if bits > maxIP:
        maxIP = bits

ans = []
for m in range(33):
    mask = ((1 << 32) - 1) if m == 0 else ((1 << 32) - 1) ^ ((1 << m) - 1)
    if (minIP & mask) + (1 << m) > maxIP:
        ans.append(minIP & mask)
        ans.append(mask)
        break

for address in ans:
    print(bit_to_ip(address))