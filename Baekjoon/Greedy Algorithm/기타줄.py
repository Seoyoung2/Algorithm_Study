# https://www.acmicpc.net/problem/1049

from sys import stdin

n, m = map(int, stdin.readline().split())
six, one = 1000, 1000
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    six = a if a < six else six
    one = b if b < one else one

ans = 0
if six > one * 6:
    ans = n * one
else:
    ans = six * (n // 6)
    if six > one * (n % 6):
        ans += one * (n % 6)
    else:
        ans += six
print(ans)
