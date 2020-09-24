# https://www.acmicpc.net/problem/10974

from sys import stdin
from itertools import permutations

N = int(stdin.readline())

for case in permutations(range(1, N+1)):
    print(*case)
