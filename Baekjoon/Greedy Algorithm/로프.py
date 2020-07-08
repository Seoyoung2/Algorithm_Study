# https://www.acmicpc.net/problem/2217

from sys import stdin

n = int(stdin.readline())
L = [int(stdin.readline()) for _ in range(n)]
L.sort(reverse=True)

for i in range(n):
    L[i] *= (i+1)
print(max(L))