# https://www.acmicpc.net/problem/5014
# BFS로만 가능한 문제. (DFS를 쓰면 어떤 층에 도달하는 방법이 여럿 있을 때, 처음 도달한 방법보다 나중에 도달한 방법이 더 짧을 수도 있는데도 그 경우를 탐색하지 않게 되기 때문)

from sys import stdin
from collections import deque

# 총 f층, 현재 s층, 목적지 g층
f, s, g, u, d = map(int, stdin.readline().split())
graph = [-1 for _ in range(f+1)]

ans = "use the stairs"
queue = deque([s])
graph[s] = 0
while queue:
    x = queue.popleft()
    if x == g:
        ans = graph[x]
        break
    for dx in [u, -d]:
        if 1 <= x+dx <= f and graph[x+dx] == -1:
            graph[x+dx] = graph[x] + 1
            queue.append(x+dx)
print(ans)
