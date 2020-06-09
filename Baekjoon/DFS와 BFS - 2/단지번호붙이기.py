# https://www.acmicpc.net/problem/2667

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
for _ in range(n):
    graph.append(stdin.readline().rstrip())
queue = deque([])
cnt, answer = 0, []
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visit[i][j] == 0:
            cnt += 1
            answer.append(1)
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                visit[x][y] = cnt
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        if graph[x + dx][y + dy] == '1' and visit[x + dx][y + dy] == 0:
                            queue.append((x + dx, y + dy))
                            visit[x + dx][y + dy] = cnt
                            answer[cnt-1] += 1
print(cnt)
for i in sorted(answer):
    print(i)