# https://www.acmicpc.net/problem/2588

from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())

for i in range(3):
    print(a * int(str(b)[2-i]))
print(a * b)