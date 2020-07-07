# https://www.acmicpc.net/problem/2468
# BFS로 풀었을 때보다 시간이 너무 오래걸림(DFS)

from sys import stdin

n = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(n)]


def dfs(x, y, height):
    visit[x][y] = 1
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if L[x+dx][y+dy] > height and not visit[x+dx][y+dy]:
                dfs(x+dx, y+dy, height)


ans = 0
high = max(num for row in L for num in row)
for h in range(0, high):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] > h and not visit[i][j]:
                cnt += 1
                dfs(i, j, h)
    ans = max(ans, cnt)
print(ans)
