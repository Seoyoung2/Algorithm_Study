# https://www.acmicpc.net/problem/1966

from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    ans = []
    im = list(map(int, stdin.readline().split()))
    q = deque([*zip(im, range(N))])
    while q:
        x, idx = q.popleft()
        for w in q:
            if x < w[0]:
                q.append((x, idx))
                break
        else:
            # 첫번째 문서의 중요도가 제일 높으면
            ans.append(idx)
    print(ans.index(M)+1)
