from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
t = int(stdin.readline())


def dfs(ii, jj):
    graph[ii][jj] = 0
    xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x, y in xy:
        if 0 <= ii + x < n and 0 <= jj + y < m:
            if graph[ii + x][jj + y] == 1:
                dfs(ii+x, jj+y)


for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        graph[b][a] = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                ans += 1
                dfs(i, j)
    print(ans)


# 단지번호붙이기와 매우 비슷한 문제로, DFS와 재귀를 이용했다.
# 처음 시도에서 런타임에러가 나서 찾아보니 "파이썬 재귀 최대깊이 지정"이 필요했다.
# ====> import sys / sys.setrecursionlimit(limit)
