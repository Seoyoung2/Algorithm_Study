# https://www.acmicpc.net/problem/3055


from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(r)]
visit = [[0] * c for _ in range(r)]

now = deque([(x, y) for x in range(len(graph)) for y in range(len(graph[x])) if graph[x][y] == 'S'])
water = deque([(x, y) for x in range(len(graph)) for y in range(len(graph[x])) if graph[x][y] == '*'])


def bfs():
    time = 0
    visit[now[0][0]][now[0][1]] = 1
    while now:
        time += 1
        # water 전파
        for _ in range(len(water)):
            x, y = water.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                if 0 <= x+dx < r and 0 <= y+dy < c:
                    if graph[x+dx][y+dy] == '.':
                        graph[x+dx][y+dy] = '*'
                        water.append((x+dx, y+dy))
        # 고슴도치 이동
        for _ in range(len(now)):
            x, y = now.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                # 갈 수 있는 구역인 경우 (상/하/좌/우)
                if 0 <= x+dx < r and 0 <= y+dy < c:
                    if graph[x+dx][y+dy] == 'D':
                        return time
                    elif graph[x+dx][y+dy] == '.' and visit[x+dx][y+dy] == 0:
                        now.append((x+dx, y+dy))
                        visit[x+dx][y+dy] = 1
    return 'KAKTUS'


print(bfs())
