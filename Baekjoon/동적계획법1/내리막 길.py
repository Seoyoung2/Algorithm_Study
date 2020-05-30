# 힘들었던 문제

# DFS만을 이용해서 풀었을 때, 답은 맞았지만 시간초과로 통과하지 못했다.
# 그래서 DP를 사용했고, *** 노드가 방문한 노드인지 체크해야한다***

# 그래도 계속 런타임에러 나서 찾아보니 재귀깊이설정이 필요한 문제였음,,

# dp[i][j] : (i, j)까지의 경로의 수


from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

m, n = map(int, stdin.readline().split())
data = [list(map(int, stdin.readline().split())) for _ in range(m)]

# dxdy = (1, 0), (-1, 0), (0, 1), (0, -1)
dp = [[-1] * n for _ in range(m)]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        if x - 1 >= 0 and data[x][y] > data[x - 1][y]:
            dp[x][y] += dfs(x - 1, y)
        if x + 1 < m and data[x][y] > data[x + 1][y]:
            dp[x][y] += dfs(x + 1, y)
        if y - 1 >= 0 and data[x][y] > data[x][y - 1]:
            dp[x][y] += dfs(x, y - 1)
        if y + 1 < n and data[x][y] > data[x][y + 1]:
            dp[x][y] += dfs(x, y + 1)
    return dp[x][y]


print(dfs(0, 0))


#stack = [(0, 0)]
# ans = 0
# while stack:
#     x, y = stack.pop()
#     if x == m-1 and y == n-1:
#         ans += 1
#         continue
#     for dx, dy in dxdy:
#         if x+dx < 0 or x+dx >= m or y+dy < 0 or y+dy >= n:
#             continue
#         if data[x+dx][y+dy] < data[x][y]:
#             stack.append((x + dx, y + dy))
# print(ans)
