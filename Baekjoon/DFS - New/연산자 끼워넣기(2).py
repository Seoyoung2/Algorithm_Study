# https://www.acmicpc.net/problem/15658

import sys
from math import inf
sys.setrecursionlimit(10**6)


def dfs(cnt, res):
    global rmax, rmin, add, sub, mul, div
    if cnt == N:
        rmax = max(rmax, res)
        rmin = min(rmin, res)
        return
    if add:
        add -= 1
        dfs(cnt + 1, res + num[cnt])
        add += 1
    if sub:
        sub -= 1
        dfs(cnt + 1, res - num[cnt])
        sub += 1
    if mul:
        mul -= 1
        dfs(cnt + 1, res * num[cnt])
        mul += 1
    if div:
        div -= 1
        dfs(cnt + 1, res // num[cnt] if res > 0 else -((-res) // num[cnt]))
        div += 1


N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

rmax, rmin = -inf, inf
dfs(1, num[0])
print(rmax)
print(rmin)
