# https://www.acmicpc.net/problem/2869

from sys import stdin
from math import ceil

A, B, V = map(int, stdin.readline().split())

print(ceil((V-A)/(A-B)) + 1)