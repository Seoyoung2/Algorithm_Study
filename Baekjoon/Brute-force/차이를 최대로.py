# https://www.acmicpc.net/problem/10819

from sys import stdin
from itertools import permutations


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

ans = 0
for case in permutations(A):
    tmp = 0
    for i in range(1, N):
        tmp += abs(case[i-1] - case[i])
    ans = max(ans, tmp)

print(ans)