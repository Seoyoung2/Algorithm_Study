# https://www.acmicpc.net/problem/1712

from sys import stdin

a, b, c = map(int, stdin.readline().split())

print(-1) if b >= c else print(a//(c-b) + 1)