# https://www.acmicpc.net/problem/16928

from collections import deque


N, M = map(int, input().split())
jump = {}
for _ in range(N+M):
    x, y = map(int, input().split())
    jump[x] = y

time = [-1] * 101
time[1] = 0

q = deque([1])
while q:
    x = q.popleft()
    for i in range(1, 7):
        nx = x + i
        if nx > 100: continue
        if nx in jump:
            nx = jump[nx]
        if time[nx] == -1:
            time[nx] = time[x] + 1
            q.append(nx)
print(time[100])

