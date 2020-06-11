# https://www.acmicpc.net/problem/2583

from sys import stdin

m, n, k = map(int, stdin.readline().split())
visit = [[0] * n for _ in range(m)]
graph = [[1] * n for _ in range(m)]
# 주어진 좌표로 graph 구성하기
for _ in range(k):
    a, b, c, d = map(int, stdin.readline().split())
    # graph[b][a]부터 graph[d-1][c-1]
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 0
# graph에서 분리된 영역 찾기 (1의 개수)
ans = []
for i in range(m):
    for j in range(n):
        if graph[i][j] and visit[i][j] == 0:
            cnt = 0
            stack = [(i, j)]
            visit[i][j] = 1
            while stack:
                cnt += 1
                x, y = stack.pop()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if graph[x + dx][y + dy] and visit[x + dx][y + dy] == 0:
                            stack.append((x + dx, y + dy))
                            visit[x + dx][y + dy] = 1
            ans.append(cnt)
print(len(ans))
for num in sorted(ans):
    print(num, end=" ")


