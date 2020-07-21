# https://www.acmicpc.net/problem/1389
# 이런 최단거리 문제는 dfs보다 bfs가 훨훨훨후러씬 편하고 쉽다..
# dfs로 푸는거 다시 해봐야할 듯 ㅠㅠ

from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


ans = -1
visit = [0] * (N+1)


def dfs(x, y, cnt):
    global tmp
    if x == y:
        tmp = min(tmp, cnt)
        return
    for n in graph[x]:
        if visit[n] == 0:
            visit[x] = 1
            dfs(n, y, cnt+1)
            visit[x] = 0


res = 999999
for i in range(1, N+1):
    bacon = 0
    for j in range(1, N+1):
        if i != j:
            tmp = 999999
            dfs(i, j, 0)
            bacon += tmp
    if bacon < res:
        res = bacon
        ans = i

print(ans)
