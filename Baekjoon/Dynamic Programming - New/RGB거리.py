# https://www.acmicpc.net/problem/1149
# dp[n][m] = min(dp[n-1]) +

from sys import stdin

n = int(stdin.readline())
graph = [[0, 0, 0]] + [[] for _ in range(n)]
for i in range(1, n+1):
    graph[i] = list(map(int, stdin.readline().split()))
    for j in range(3):
        graph[i][j] += min(graph[i-1][:j] + graph[i-1][j+1:])
print(min(graph[-1]))