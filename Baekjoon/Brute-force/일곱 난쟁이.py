# https://www.acmicpc.net/problem/2309

from sys import stdin
from itertools import combinations

H = [int(stdin.readline()) for _ in range(9)]

for case in combinations(H, 7):
    if sum(case) == 100:
        ans = sorted(case)
        break

for i in ans:
    print(i)
