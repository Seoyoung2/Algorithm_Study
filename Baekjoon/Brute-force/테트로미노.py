# https://www.acmicpc.net/problem/14500
# bfs..? bfs 쓰면 'ㅗ'모양 불가능 -> 예외처리 해줘야함

from sys import stdin

N, M = map(int, stdin.readline().split())
score = [list(map(int, stdin.readline().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

ohs = [[(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, 1)],
       [(0, 1), (0, 2), (-1, 1)], [(1, 0), (2, 0), (1, -1)]]


def dfs(x, y, cnt, n):
    global ans
    if cnt == 4:
        ans = max(ans, n)
        return
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < N and 0 <= y+dy < M and not visit[x+dx][y+dy]:
            visit[x+dx][y+dy] = 1
            dfs(x+dx, y+dy, cnt+1, n+score[x+dx][y+dy])
            visit[x+dx][y+dy] = 0


def check_oh(x, y):
    global ans
    for oh in ohs:
        # for문보다 try-except이 적은 시간 걸림
        # tmp = score[x][y]
        # for dx, dy in oh:
        #     if 0 <= x+dx < N and 0 <= y+dy < M:
        #         tmp += score[x+dx][y+dy]
        #     else:
        #         tmp = 0
        #         break
        try:
            tmp = score[x][y] + score[x+oh[0][0]][y+oh[0][1]] + score[x+oh[1][0]][y+oh[1][1]] + score[x+oh[2][0]][y+oh[2][1]]
        except:
            tmp = 0
        ans = max(ans, tmp)


ans = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, 1, score[i][j])
        visit[i][j] = 0
        check_oh(i, j)
print(ans)
