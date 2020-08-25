# https://www.acmicpc.net/problem/1874
# 1 2 5 6
# 4 3

from sys import stdin

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]

stack = []
ans = []
idx = 0
for i in range(1, n+1):
    stack.append(i)
    ans.append("+")
    while stack and stack[-1] == nums[idx]:
        stack.pop()
        ans.append("-")
        idx += 1

if stack:
    print("NO")
else:
    for res in ans:
        print(res)
        