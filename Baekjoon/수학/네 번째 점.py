# https://www.acmicpc.net/problem/3009

from sys import stdin

res = [[], []]
for _ in range(3):
    x, y = map(int, stdin.readline().split())
    res[0].append(x) if x not in res[0] else res[0].remove(x)
    res[1].append(y) if y not in res[1] else res[1].remove(y)
print(*res[0], *res[1])
