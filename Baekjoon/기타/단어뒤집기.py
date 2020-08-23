# https://www.acmicpc.net/problem/9093

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    S = stdin.readline().split()
    for word in S:
        print(word[::-1], end=" ")
    print()
