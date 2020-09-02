# https://www.acmicpc.net/problem/11576

from sys import stdin

A, B = map(int, stdin.readline().split())
m = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

res = 0
for i, x in enumerate(nums[::-1]):
    res += x * (A ** i)

ans = []
while res >= B:
    ans.append(res % B)
    res //= B
ans.append(res)

print(*ans[::-1])