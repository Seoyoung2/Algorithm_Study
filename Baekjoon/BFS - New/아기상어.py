# https://www.acmicpc.net/problem/16236

from collections import deque
from math import inf


def bfs(tmap, eat, baby):
    global space
    # 아기상어부터 각 구역의 거리 측정
    q = deque([baby])
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and tmap[nx][ny] == -1:
                tmap[nx][ny] = tmap[x][y] + 1
                q.append((nx, ny))

    # 먹잇감 중 갈 수 있고 가장 가까운 먹잇감 고르기
    res = inf
    candi = []
    for e in eat:
        ex, ey = e[0], e[1]
        if tmap[ex][ey] > 0:
            if tmap[ex][ey] < res:
                res = tmap[ex][ey]
                candi = [(ex, ey)]
            elif tmap[ex][ey] == res:
                candi.append((ex, ey))
    # 갈 수 있는 먹잇감이 없다면
    if not candi:
        return False
    candi.sort()
    space[baby[0]][baby[1]] = 0
    space[candi[0][0]][candi[0][1]] = 9
    return res if res > 0 else False


def make_map(big, map):
    tmp = [[0] * N for _ in range(N)]
    eat = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == 9:      # 아기상어
                baby = (i, j)
                tmp[i][j] = 0
            elif map[i][j] > big:   # 벽
                tmp[i][j] = -2
            elif map[i][j] and map[i][j] < big:   # 먹이
                tmp[i][j] = -1
                eat.append((i, j))
            else:
                tmp[i][j] = -1
    if not eat:
        return False
    return bfs(tmp, eat, baby)


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

big = 2
ans, flag = 0, 0
while True:
    a = make_map(big, space)
    if not a:
        break
    ans += a
    flag += 1
    if flag == big:
        big += 1
        flag = 0
print(ans)
