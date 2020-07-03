# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().split())
origin = [list(map(int, stdin.readline().split())) for _ in range(n)]

# 조합으로 벽 3개 세우고 -> 바이러스 기준으로 BFS -> 0의 개수 max인 경우 구하기
space, virus = [], deque()
answer = 0
for i in range(n):
    for j in range(m):
        if origin[i][j] == 0:
            space.append((i, j))
        elif origin[i][j] == 2:
            virus.append((i, j))

for wall in combinations(space, 3): #( (1,2), (3,4), (1,3) )
    case = [origin[i][:] for i in range(n)]
    for i in range(3):
        case[wall[i][0]][wall[i][1]] = 1

    # BFS
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if case[x + dx][y + dy] == 0:
                    queue.append((x+dx, y+dy))
                    case[x+dx][y+dy] = 2

    # space 개수 세기
    res = 0
    for c in case:
        res += c.count(0)
    answer = max(answer, res)
print(answer)
