# https://www.acmicpc.net/problem/11403
# 방향이 있는 그래프라는 점!

from sys import stdin
from collections import deque

n = int(stdin.readline())
road = {i: [] for i in range(1, n+1)}
graph = [['0'] * n for _ in range(n)]

# Make ROAD Dictionary
for i in range(1, n+1):
    tmp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if tmp[j]:
            road[i].append(j+1)
# BFS
for i in range(1, n+1):
    queue = deque([i])
    while queue:
        start = queue.popleft()
        for j in road[start]:
            if graph[i-1][j-1] == '0':
                graph[i-1][j-1] = '1'
                queue.extend(road[start])
# print
for row in graph:
    print(" ".join(row))
