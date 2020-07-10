# https://www.acmicpc.net/problem/2529
# 백트래킹으로는 너무너무 어려워서 순열을 사용해봄

from sys import stdin
from itertools import permutations

k = int(stdin.readline())
L = stdin.readline().split()
ans = []
for nums in permutations(range(0, 10), k+1):
    for i in range(k):
        if (L[i] == '<' and nums[i] > nums[i+1]) or (L[i] == '>' and nums[i] < nums[i+1]):
            break
    else:
        ans.append(nums)
ans.sort()
print("".join(map(str, ans[-1])))
print("".join(map(str, ans[0])))
