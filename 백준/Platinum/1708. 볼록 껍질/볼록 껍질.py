import sys
from math import atan2
input = sys.stdin.readline

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])


def dist2(a, b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return (dx ** 2 + dy ** 2) ** 0.5
  

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]

pivot = min(pts, key=lambda p: (p[1], p[0]))

pts.remove(pivot)

pts.sort(key=lambda p: (atan2((p[1] - pivot[1]), (p[0] - pivot[0])), dist2(p, pivot)))

hull = [pivot]
for p in pts:
    while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
        hull.pop()
    hull.append(p)

print(len(hull))