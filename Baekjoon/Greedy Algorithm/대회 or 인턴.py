# https://www.acmicpc.net/problem/2875

from sys import stdin

n, m, k = map(int, stdin.readline().split())
# n명 중 2명, m명 중 1명, k명 빠지기
ans = 0
while True:
    if n < 2 or m < 1 or n + m - 3 < k:
        break
    n -= 2
    m -= 1
    ans += 1
print(ans)