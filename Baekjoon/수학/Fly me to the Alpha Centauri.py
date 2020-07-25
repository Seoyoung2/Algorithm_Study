# https://www.acmicpc.net/problem/1011
# 이걸 어떻게 생각하지,, math
# [1, 2, 3, ..., (n-1), n, (n-1), ..., 2, 1]
# 이 배열의 합 = n(n+1)/2 + n(n-1)/2 = n*n

from sys import stdin
import math

T = int(stdin.readline())
for _ in range(T):
    x, y = map(int, stdin.readline().split())
    n = int(math.sqrt(y-x))
    # 1-1(1) / 2-1,2,1(3) / 3-1,2,3,2,1(5)
    print((y - x) - n + 1)
    print()
