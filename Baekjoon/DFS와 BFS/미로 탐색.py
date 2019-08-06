# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.


from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append([])
    tmp = str(stdin.readline().rstrip())
    for j in range(m):
        graph[i].append(int(tmp[j]))

dxdy = (1, 0), (-1, 0), (0, 1), (0, -1)
queue = [(0, 0)]
visit = [[0]*m for _ in range(n)]
visit[0][0] = 1
while queue:
    x, y = queue.pop(0)
    for dx, dy in dxdy:
        if 0 <= x+dx < n and 0 <= y+dy < m:
            if graph[x+dx][y+dy] and visit[x+dx][y+dy] == 0:
                visit[x+dx][y+dy] = visit[x][y] + 1
                queue.append((x+dx, y+dy))

print(visit[-1][-1])


# 최단거리 문제이기 때문에 BFS를 이요했다. 2차원 배열 visit에다가 지금까지 온 거리를 기록했다.
