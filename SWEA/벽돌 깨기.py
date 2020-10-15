# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo

from itertools import product

T = int(input())


def dfs(tx, ty, tW):
    n = tW[tx][ty]
    tW[tx][ty] = 0
    for i in range(1, n):
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= tx+dx*i < H and 0 <= ty+dy*i < W:
                dfs(tx+dx*i, ty+dy*i, tW)


def clean_wall(tW):
    for i in range(W):
        tmp = []
        for j in range(H-1, -1, -1):
            if tW[j][i]:
                tmp.append(tW[j][i])
                tW[j][i] = 0
        idx = H - 1
        for j in tmp:
            tW[idx][i] = j
            idx -= 1


def drop(x, W):
    for i in range(H):
        if W[i][x]:
            dfs(i, x, W)
            clean_wall(W)
            break


for t in range(1, T+1):
    ans = 180
    N, W, H = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(H)]
    for case in product([n for n in range(W)], repeat=N):
        twall = [row[:] for row in wall]
        for c in case:
            drop(c, twall)
        cnt = 0
        for row in twall:
            cnt += row.count(0)
        ans = min(ans, W*H - cnt)
    print("#{} {}".format(t, ans))