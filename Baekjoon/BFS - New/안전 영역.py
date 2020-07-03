# https://www.acmicpc.net/problem/2468

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph, res = [], 0
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

high = max(num for row in graph for num in row)
# 비가 안오는 경우도 생각해야 하기 때문에 0부터 시작
for h in range(0, high):
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # BFS (기준 높이보다 큰 구역만 체크해서 한번에 개수 세기)
            if graph[i][j] > h and visit[i][j] == 0:
                queue = deque([(i, j)])
                visit[i][j] = 1
                cnt += 1
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        if 0 <= x+dx < n and 0 <= y+dy < n:
                            if graph[x+dx][y+dy] > h and visit[x+dx][y+dy] == 0:
                                queue.append((x+dx, y+dy))
                                visit[x+dx][y+dy] = 1
    res = max(res, cnt)
print(res)