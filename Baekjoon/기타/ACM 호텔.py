# https://www.acmicpc.net/problem/10250

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    h, w, n = map(int, stdin.readline().split())
    flo = str(n % h) if n % h != 0 else str(h)
    ho = str(1 + n // h) if n % h != 0 else str(h)
    print("".join(flo + "0" + ho)) if len(ho) == 1 else print("".join(flo + ho))
