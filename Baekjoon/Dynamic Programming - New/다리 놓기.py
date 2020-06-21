# https://www.acmicpc.net/problem/1010

from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    ans = 1
    n, m = map(int, stdin.readline().split())
    if n > m-n:
        n = m - n
    for i in range(m, m-n, -1):
        ans *= i
    for i in range(n, 1, -1):
        ans //= i
    print(ans)
