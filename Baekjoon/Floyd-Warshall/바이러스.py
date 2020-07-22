# https://www.acmicpc.net/problem/2606

from sys import stdin

v = int(stdin.readline())
e = int(stdin.readline())
graph = [[100] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for num in graph[1]:
    if num < 100:
        ans += 1
print(ans-1)
