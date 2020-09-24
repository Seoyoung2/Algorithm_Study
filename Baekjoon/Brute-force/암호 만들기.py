# https://www.acmicpc.net/problem/1759
# 모음 1개 이상 + 자음 2개 이상

from sys import stdin
from itertools import combinations

L, C = map(int, stdin.readline().split())
chs = sorted(stdin.readline().split())

# 자음 2개 이상을 체크하지 못함
# mos = ['a', 'e', 'i', 'o', 'u']
# for case in combinations(chs, L):
#     if any(mo in case for mo in mos):
#         print("".join(case))

mos = ['a', 'e', 'i', 'o', 'u']
for case in combinations(chs, L):
    cnt = 0
    for mo in mos:
        if mo in case:
            cnt += 1
    if cnt >= 1 and L-cnt >= 2:
        print("".join(case))
