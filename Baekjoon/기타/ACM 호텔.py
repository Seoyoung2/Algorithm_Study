# https://www.acmicpc.net/problem/10250

from sys import stdin
from math import ceil

T = int(stdin.readline())
for _ in range(T):
    h, w, n = map(int, stdin.readline().split())
    flo = str(n % h) if n % h != 0 else str(h)
    ho = str(ceil(n / h))
    print("".join(flo + "0" + ho)) if len(ho) == 1 else print("".join(flo + ho))

# 6 12 10 => 402
# 30 50 72 => 1203
# 1 1 1 => 101
# 6 5 6 => 601
# 6 5 12 => 602
# 6 5 10 => 402
