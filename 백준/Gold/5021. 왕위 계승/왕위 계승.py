from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
king = input().strip()

children = defaultdict(list)
indegree = defaultdict(int)
blood = defaultdict(float)

blood[king] = 1.0
for _ in range(n):
    child, *parents = input().split()
    for parent in parents:
        children[parent].append(child)
        indegree[parent] += 0

    indegree[child] += 2


q = deque()
for person in indegree:
    if indegree[person] == 0:
        q.append(person)

while q:
    who = q.popleft()
    for child in children[who]:
        blood[child] += blood[who] / 2
        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)

ans = None
MAX_BLOOD = -1
for _ in range(m):
    prince = input().strip()
    b = blood.get(prince, -1)
    if b > MAX_BLOOD:
        MAX_BLOOD = b
        ans = prince

print(ans)