# https://www.acmicpc.net/problem/2798

from sys import stdin

n, m = map(int, stdin.readline().split())
L = list(map(int, stdin.readline().split()))

res = 0
for i in L:
    for j in L:
        for k in L:
            if i == j or i == k or j == k:
                break
            if res < i + j + k <= m:
                res = i + j + k
print(res)