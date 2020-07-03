# https://www.acmicpc.net/problem/1697

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

# n -> (n+1, n-1, 2*n)

queue = deque([n])
visited = {n: 0}
while queue:
    x = queue.popleft()
    if x == k:
        break
    for i in [x-1, x+1, 2*x]:
        if i not in visited and 0 <= i <= 100000:
            queue.append(i)
            visited[i] = visited[x] + 1

print(visited[k])