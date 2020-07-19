# https://www.acmicpc.net/problem/2562

from sys import stdin

nums = [int(stdin.readline()) for _ in range(9)]
ans, ans2 = 0, 0
for idx, x in enumerate(nums):
    if x > ans:
        ans = x
        ans2 = idx + 1
print(ans)
print(ans2)