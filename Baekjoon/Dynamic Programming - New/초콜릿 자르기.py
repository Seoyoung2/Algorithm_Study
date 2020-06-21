# https://www.acmicpc.net/problem/2163
# DP 문제지만 걍 n*m-1 하면 끝

from sys import stdin
n, m = map(int, stdin.readline().split())
print(n*m-1)
