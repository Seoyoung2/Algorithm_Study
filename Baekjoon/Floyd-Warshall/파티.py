# https://www.acmicpc.net/problem/1238

from sys import stdin
from math import inf

n, m, x = map(int, stdin.readline().split())
T = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, stdin.readline().split())
    T[a-1][b-1] = t

res = [inf] * n
for k in range(n):
    for i in range(n):
        for j in range(n):
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])
            res[i] = min(res[i], T[i][j] + T[j][i])

print(max(res))

# 플로이드 알고리즘으로 문제풀면 시간초과,,,,,, 다익스트라 공부하고 그걸로 해야할 듯!
