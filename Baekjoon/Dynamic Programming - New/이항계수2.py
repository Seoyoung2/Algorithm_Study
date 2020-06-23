# https://www.acmicpc.net/problem/11051

from sys import stdin

n, k = map(int, stdin.readline().split())
ans = 1
for i in range(n, n - k, -1):
    ans *= i
for i in range(k, 1, -1):
    ans //= i
print(ans % 10007)