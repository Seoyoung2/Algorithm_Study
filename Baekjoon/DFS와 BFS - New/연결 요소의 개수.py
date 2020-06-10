# https://www.acmicpc.net/problem/11724
# BFS/DFS를 쓰는 방법도 있지만 Union-Find(합집합 찾기)를 사용함

from sys import stdin

n, m = map(int, stdin.readline().split())
parent = {i: i for i in range(1, n+1)}


def getParent(n):
    if n == parent[n]:
        return n
    parent[n] = getParent(parent[n])
    return parent[n]


for i in range(m):
    a, b = map(int, stdin.readline().split())
    pa, pb = getParent(a), getParent(b)
    if pa > pb:
        parent[pa] = pb
    elif pa < pb:
        parent[pb] = pa
    print(parent)

ans = set()
for x in range(1, n+1):
    ans.add(getParent(x))
print(len(ans))
