# https://www.acmicpc.net/problem/1389

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# 최단경로 구하기 (BFS)
ans = []
for i in range(1, n+1):
    visit = [-1 for _ in range(n + 1)]
    queue = deque([i])
    visit[i] = 0
    while queue:
        x = queue.popleft()
        for next in graph[x]:
            if visit[next] == -1:
                queue.append(next)
                visit[next] = visit[x] + 1
    ans.append(sum(visit) + 1)
print(ans.index(min(ans)) + 1)
