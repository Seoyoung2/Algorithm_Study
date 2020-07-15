# https://www.acmicpc.net/problem/2884

from sys import stdin

hour, min = map(int, stdin.readline().split())
if min >= 45:
    min -= 45
else:
    min = min - 45 + 60
    hour -= 1
    if hour < 0:
        hour +=  24
print(hour, min)