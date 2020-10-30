# https://www.acmicpc.net/problem/13913
# bfs로 최단거리 구하고 dfs로 경로..? / bfs로 최단거리 구할때 이전 위치 저장?

from collections import deque

N, K = map(int, input().split())
ans = 0

# BFS
check = [-1] * 100001
check[N] = 0
q = deque([(N, 0)])
while q:
    x, step = q.popleft()
    if x == K:
        ans = step
        break
    for n in (x-1, x+1, x+x):
        if 0 <= n < 100001 and check[n] == -1:
            q.append((n, step+1))
            check[n] = x
print(ans)
route = deque([K])
for _ in range(ans):
    K = check[K]
    route.appendleft(K)
print(*route)
