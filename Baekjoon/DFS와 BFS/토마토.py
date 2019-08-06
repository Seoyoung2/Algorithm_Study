from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
graph = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    line = [-1]
    line.extend([int(x) for x in stdin.readline().split()])
    line.append(-1)
    graph.append(line)
graph.append([-1 for _ in range(m + 2)])

queue = deque()
for col in range(1, m + 1):
    for row in range(1, n + 1):
        if graph[row][col] == 1:
            queue.append((row, col))

ans = 1
while queue:
    x, y = queue.popleft()
    ans = graph[x][y]
    # for dx, dy in dxdy:
    #     if 0 <= x+dx < n and 0 <= y+dy < m:
    #         if graph[x+dx][y+dy] == 0:
    #             ans = graph[x][y] + 1
    #             graph[x+dx][y+dy] = ans
    #             queue.append((x+dx, y+dy))
    if graph[x - 1][y] == 0:
        graph[x - 1][y] = graph[x][y] + 1
        queue.append((x - 1, y))
    if graph[x + 1][y] == 0:
        graph[x + 1][y] = graph[x][y] + 1
        queue.append((x + 1, y))
    if graph[x][y - 1] == 0:
        graph[x][y - 1] = graph[x][y] + 1
        queue.append((x, y - 1))
    if graph[x][y + 1] == 0:
        graph[x][y + 1] = graph[x][y] + 1
        queue.append((x, y + 1))
# t = True
# for i in range(n):
#     if 0 in graph[i]:
#         print(-1)
#         t = False
#         break
# if t:
#     print(ans-1)
print(ans - 1 if all(0 not in row for row in graph) else -1)


# 최단거리 문제. BFS 이용했다. 뿌듯
