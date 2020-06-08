# https://www.acmicpc.net/problem/1260

from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v):
    stack = [v]
    visited = set()
    while stack:
        x = stack.pop()
        if x not in visited:
            print(x, end=" ")
            visited.add(x)
            stack.extend(sorted(graph[x], reverse=True))


def bfs(graph, v):
    queue = deque([v])
    visited = set()
    while queue:
        x = queue.popleft()
        if x not in visited:
            print(x, end=" ")
            visited.add(x)
            queue.extend(sorted(graph[x]))


dfs(graph, v)
print()
bfs(graph, v)
