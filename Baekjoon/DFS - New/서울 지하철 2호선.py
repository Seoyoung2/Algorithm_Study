# https://www.acmicpc.net/problem/16947

import sys
from collections import deque
sys.setrecursionlimit(10**6)


def dfs(cur, prev):
    if not check[cur]:      # 첫방문일 경우
        check[cur] = 1
        for n in station[cur]:
            if n == prev:
                continue
            res = dfs(n, cur)   # 순환 시작점 반환
            if res > 0:
                check[cur] = 2  # 순환선에 존재
                if cur != res:
                    return res
                else:           # 현재역이 시작점이면 stop
                    return -1
    else:
        return cur
    return -1


def bfs(tx):
    q = deque([tx])
    while q:
        x = q.popleft()
        for n in station[x]:
            if ans[n] == -1:
                ans[n] = ans[x] + 1
                q.append(n)


N = int(input())
station = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    station[a].append(b)
    station[b].append(a)

# 순환선 구하기
check = [0] * (N+1)
dfs(1, 0)
print(check)

# 각각의 거리 구하기
candi = []
ans = [-1] * (N+1)
for i in range(1, N+1):
    if check[i] == 2:
        ans[i] = 0
        if len(station[i]) > 2:
            candi.append(i)
for i in candi:
    bfs(i)
print(*ans[1:])
