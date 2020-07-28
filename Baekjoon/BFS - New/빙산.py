# https://www.acmicpc.net/problem/2573

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

queue = deque([(i, j) for i in range(n) for j in range(m) if graph[i][j] != 0])
time = 0
while True:
    if not queue:
        time = 0
        break
    # (x, y)부터 시작해서 덩어리 세기
    visit = [graph[i][:] for i in range(n)]
    stack = [queue[0]]
    while stack:
        a, b = stack.pop()
        visit[a][b] = 0
        for da, db in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= a+da < n and 0 <= b+db < m:
                if visit[a+da][b+db] > 0:
                    visit[a+da][b+db] = 0
                    stack.append((a+da, b+db))
    # 분리된 빙산이 있다면 while문 나가기
    if any(i > 0 for row in visit for i in row):
        break
    time += 1
    # 높이 줄이기
    visit = [graph[i][:] for i in range(n)]
    # while문이 아닌 for문(len(queue))을 사용함으로써 동시간대에 사라진 빙산 무시
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if not graph[x + dx][y + dy] and not visit[x + dx][y + dy]:
                    graph[x][y] -= 1
                    if graph[x][y] == 0:
                        break
        if graph[x][y] > 0:
            queue.append((x, y))
print(time)

# 처음부터 빙산이 분리되어 있으면 바로 0 출력!!
