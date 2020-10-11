# https://www.acmicpc.net/problem/13458

from sys import stdin
from math import ceil

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())

ans = 0
for n in A:
    n -= B
    if n < 0:
        n = 0
    ans += (1 + ceil(n/C))
print(ans)