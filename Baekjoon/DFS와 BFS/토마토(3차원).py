from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
graph = [[[-1 for _ in range(m + 2)] for _ in range(n+2)]]
for _ in range(h):
    face = [[-1 for _ in range(m + 2)]]
    for _ in range(n):
        line = [-1]
        line.extend([int(x) for x in stdin.readline().split()])
        line.append(-1)
        face.append(line)
    face.append([-1 for _ in range(m + 2)])
    graph.append(face)
graph.append([[-1 for _ in range(m + 2)] for _ in range(n+2)])

q = deque()
for col in range(1, m + 1):
    for row in range(1, n + 1):
        for ax in range(1, h + 1):
            if graph[ax][row][col] == 1:
                q.append((ax, row, col))

ans = 1
while q:
    z, x, y = q.popleft()
    ans = graph[z][x][y]
    if graph[z][x - 1][y] == 0:
        graph[z][x - 1][y] = graph[z][x][y] + 1
        q.append((z, x - 1, y))
    if graph[z][x + 1][y] == 0:
        graph[z][x + 1][y] = graph[z][x][y] + 1
        q.append((z, x + 1, y))
    if graph[z][x][y - 1] == 0:
        graph[z][x][y - 1] = graph[z][x][y] + 1
        q.append((z, x, y - 1))
    if graph[z][x][y + 1] == 0:
        graph[z][x][y + 1] = graph[z][x][y] + 1
        q.append((z, x, y + 1))
    if graph[z - 1][x][y] == 0:
        graph[z - 1][x][y] = graph[z][x][y] + 1
        q.append((z - 1, x, y))
    if graph[z + 1][x][y] == 0:
        graph[z + 1][x][y] = graph[z][x][y] + 1
        q.append((z + 1, x, y))

check = True
for i in range(1, h+1):
    for j in range(1, n+1):
        if 0 in graph[i][j]:
            print(-1)
            check = False
            break
    if not check:
        break
if check:
    print(ans-1)
