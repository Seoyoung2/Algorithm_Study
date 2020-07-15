# https://www.acmicpc.net/problem/11021

from sys import stdin

t = int(stdin.readline())
for i in range(t):
    a, b = map(int, stdin.readline().split())
    print("Case #{}: {}".format(i+1, a+b))