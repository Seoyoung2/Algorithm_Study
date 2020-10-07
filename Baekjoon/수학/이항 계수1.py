# https://www.acmicpc.net/problem/11050

from sys import stdin

N, K = map(int, stdin.readline().split())
ans = 1
for n in range(N, N-K, -1):
    ans *= n
for k in range(K, 0, -1):
    ans //= k

print(ans)