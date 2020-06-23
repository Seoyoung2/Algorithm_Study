# https://www.acmicpc.net/problem/2167

from sys import stdin

n, m = map(int, stdin.readline().split())
L = [list(map(int, stdin.readline().split())) for _ in range(n)]
t = int(stdin.readline())
for _ in range(t):
    ans = 0
    sx, sy, ex, ey = map(int, stdin.readline().split())
    for x in range(sx-1, ex):
        for y in range(sy-1, ey):
           ans += L[x][y]
    print(ans)