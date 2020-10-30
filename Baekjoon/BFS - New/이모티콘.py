# https://www.acmicpc.net/problem/14226

import sys
sys.setrecursionlimit(10**6)


def emoji(out, v, cnt):
    if check[out] > cnt or not check[out]:
        check[out] = cnt
    if out > 1 and (not check[out-1] or check[out-1] > cnt+1):
        emoji(out-1, v, cnt+1)
    if out+v < 1001 and v > 0:
        emoji(out+v, v, cnt+1)
    if out+out < 1001 and out > 0:
        emoji(out+out, out, cnt+2)


S = int(input())
check = [0] * 1001
check[1] = 1
emoji(2, 1, 2)
print(check[S])


