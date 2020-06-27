# https://www.acmicpc.net/problem/1915

from sys import stdin

n, m = map(int, stdin.readline().split())
L = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if L[i][j]:
            L[i][j] += min(L[i-1][j], L[i][j-1], L[i-1][j-1])
print(max([max(row) for row in L]) ** 2)
