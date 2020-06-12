# https://www.acmicpc.net/problem/2644

from sys import stdin
from collections import deque

n = int(stdin.readline())
start, end = map(int, stdin.readline().split())
m = int(stdin.readline())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

if start == end:
    print(0)
    exit()

# BFS
queue = deque()
for i in range(n+1):
    if graph[start][i]:
        queue.append(i)
        while queue:
            x = queue.popleft()
            if x == end:
                break
            for j in range(n+1):
                if graph[x][j] == 1 and graph[start][j] == 0:
                    queue.append(j)
                    graph[start][j] = graph[start][x] + 1
print(graph[start][end] if graph[start][end] else -1)
