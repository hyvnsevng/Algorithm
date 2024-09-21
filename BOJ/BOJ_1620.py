# 백준 1620번 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

poke_list = []
poke_dict = dict()
for i in range(n):
    pokemon = input().strip()
    poke_list.append(pokemon)
    poke_dict[pokemon] = i+1

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(poke_list[int(q)-1])
    else:
        print(poke_dict[q])
