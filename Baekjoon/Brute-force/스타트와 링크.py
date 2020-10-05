# https://www.acmicpc.net/problem/14889

from sys import stdin
from itertools import combinations
import math

N = int(stdin.readline())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]

gap = math.inf
for case in combinations(range(N), N//2):
    team1 = team2 = 0

    for s, t in combinations(case, 2):
        team1 += (S[s][t]+S[t][s])

    rcase = set(range(N)) - set(case)
    for s, t in combinations(rcase, 2):
        team2 += (S[s][t]+S[t][s])

    gap = min(gap, abs(team1-team2))
print(gap)
