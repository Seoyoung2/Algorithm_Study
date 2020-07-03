# https://www.acmicpc.net/problem/2667

from sys import stdin

n = int(stdin.readline())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]


def dfs(x, y, count):
    visit[x][y] = count
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if graph[x+dx][y+dy] == '1' and visit[x+dx][y+dy] == 0:
                ans[-1] += 1
                dfs(x+dx, y+dy, count)


cnt, ans = 0, []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visit[i][j] == 0:
            cnt += 1
            ans.append(1)
            dfs(i, j, cnt)
print(cnt)
for num in sorted(ans):
    print(num)