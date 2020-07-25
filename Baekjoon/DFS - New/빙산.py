# https://www.acmicpc.net/problem/2573

from sys import stdin

n, m = map(int, stdin.readline().split())
B = [list(map(int, stdin.readline().split())) for _ in range(n)]


def dfs(bing, x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        bing[cx][cy] = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= cx+dx <= n and 0 <= cy+dy <= m:
                if bing[cx+dx][cy+dy]:
                    stack.append((cx+dx, cy+dy))


ans = 0
while True:
    cnt = 0
    for i in range(n):
        for j in range(m):
            if B[i][j]:
                dfs(B[:][:], i, j)
                cnt += 1
    if cnt != 1:
        break

    ans += 1
    dec = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if B[i][j] and dec[i][j] == 0:
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= i + dx <= n and 0 <= j + dy <= m:
                        if B[i+dx][j+dy] == 0:
                            dec[i][j] += 1
    print(B)
    print(dec)
    print(B-dec)