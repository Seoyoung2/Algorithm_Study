# https://www.acmicpc.net/problem/10026

from sys import stdin

n = int(stdin.readline())
graph1 = list(stdin.readline() for _ in range(n))


def bfs(graph):
    cnt = 0
    stack = []
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                cnt += 1
                color = graph[i][j]     # R, G, B
                stack.append((i, j))
                visit[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        if 0 <= x + dx < n and 0 <= y + dy < n:
                            if graph[x+dx][y+dy] == color and not visit[x+dx][y+dy]:
                                visit[x+dx][y+dy] = True
                                stack.append((x+dx, y+dy))
    return cnt


print(bfs(graph1))
graph2 = []
for word in graph1[:]:
    graph2.append(word.replace('G', 'R'))
print(bfs(graph2))


