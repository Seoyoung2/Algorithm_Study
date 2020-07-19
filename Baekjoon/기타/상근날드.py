# https://www.acmicpc.net/problem/5543

from sys import stdin

A = [int(stdin.readline()) for _ in range(3)]
B = [int(stdin.readline()) for _ in range(2)]
print(min(A) + min(B) - 50)


