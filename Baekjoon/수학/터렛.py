# https://www.acmicpc.net/problem/1002

from sys import stdin
import math


def get_distance(x, y, a, b):
    return math.sqrt(((x-a)**2) + ((y-b)**2))


T = int(stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    # 중심이 (x, y)이고 반지름이 r인 원이라고 생각하면
    #   두 원이 일치하면 -1, 내접 or 외접하면 1, 만나지않으면 0, 나머지 2
    d = get_distance(x1, y1, x2, y2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d == r1+r2 or d == r1-r2 or d == r2-r1:
        print(1)
    elif d > r1+r2 or r1-r2 > d or r2-r1 > d:
        print(0)
    else:
        print(2)
