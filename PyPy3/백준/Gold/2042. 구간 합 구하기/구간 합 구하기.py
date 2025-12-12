import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr) - 1
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self._build(1, self.n, 1)


    def _build(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return
        mid = (start + end) // 2
        left, right = index * 2, index * 2 + 1
        self._build(start, mid, left)
        self._build(mid + 1, end, right)
        self.tree[index] = self.tree[left] + self.tree[right]


    def do(self, a, b, c):
        if a == 1:
            diff = c - self.arr[b]
            self.arr[b] = c
            self._update(1, 1, self.n, b, diff)
        elif a == 2:
            print(self._get_sum(1, 1, self.n, b, c))


    def _update(self, node, start, end, idx, diff):
        if idx < start or idx > end:
            return
        self.tree[node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        self._update(node * 2, start, mid, idx, diff)
        self._update(node * 2 + 1, mid + 1, end, idx, diff)


    def _get_sum(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self._get_sum(node * 2, start, mid, left, right) + self._get_sum(node * 2 + 1, mid + 1, end, left, right)


# input = open('input.txt', 'r').readline
N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
st = SegmentTree(arr)

for _ in range(M+K):
    st.do(*map(int, input().split()))
