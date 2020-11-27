# https://www.acmicpc.net/problem/1963

from math import sqrt
from collections import deque


def bfs(start, goal):
    visit = [False] * 10000
    q = deque([(start, 0)])
    while q:
        x, n = q.popleft()
        if x == goal:
            return n
        for i in range(4):
            for j in range(10):
                xs = x[:i] + str(j) + x[i+1:]
                xi = int(xs)
                if sosu[xi] and xi >= 1000 and not visit[xi]:
                    visit[xi] = True
                    q.append((xs, n+1))


sosu = [True] * 10000
for i in range(2, int(sqrt(10000))):
    if not sosu[i]:
        continue
    for j in range(2*i, len(sosu), i):
        sosu[j] = False

T = int(input())
for _ in range(T):
    a, b = input().split()
    print(bfs(a, b))
