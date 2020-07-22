# https://www.acmicpc.net/problem/1389

from sys import stdin

n, m = map(int, stdin.readline().split())
L = [[100] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    L[a][b] = 1
    L[b][a] = 1

# 플로이드 와샬
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            L[i][j] = min(L[i][j], L[i][k]+L[k][j])

tmp, ans = 1000000, 0
for idx in range(1, n+1):
    if sum(L[idx]) < tmp:
        tmp = sum((L[idx]))
        ans = idx
print(ans)