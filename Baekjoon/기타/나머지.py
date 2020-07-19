# https://www.acmicpc.net/problem/3052

from sys import stdin

nums = [int(stdin.readline()) for _ in range(10)]
ans = set()
for n in nums:
    ans.add(n % 42)
print(len(ans))