# https://www.acmicpc.net/problem/10026

from sys import stdin

n = int(stdin.readline())
G = [stdin.readline().rstrip() for _ in range(n)]


def dfs(graph):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                cnt += 1
                stack = [(i, j)]
                visit[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        if 0 <= x+dx < n and 0 <= y+dy < n:
                            if graph[x][y] == graph[x+dx][y+dy] and not visit[x+dx][y+dy]:
                                visit[x+dx][y+dy] = 1
                                stack.append((x+dx, y+dy))
    return cnt


print(dfs(G), end=" ")
G2 = []
for row in G:
    G2.append(row.replace('G', 'R'))
print(dfs(G2))
