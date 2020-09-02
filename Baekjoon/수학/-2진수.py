# https://www.acmicpc.net/problem/2089
# 2진수: 2로 나눈 나머지로 / -2진수: -2로 나눈 나머지로?
# -13 -> 7(1) -> -3(1) -> 2(1) -> -1(0) -> 1(1)

from sys import stdin

N = int(stdin.readline())

ans = ""
while N > 1 or N < 0:
    if N % 2:
        ans += "1"
        N = N // -2 + 1
    else:
        ans += "0"
        N = N // -2

ans += "1" if N else "0"
print(ans[::-1])

