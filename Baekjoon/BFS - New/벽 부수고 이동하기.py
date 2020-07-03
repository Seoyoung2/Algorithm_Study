# https://www.acmicpc.net/problem/2206

from sys import stdin
from collections import deque

# n, m = map(int, stdin.readline().split())
# graph = [list(stdin.readline()) for _ in range(n)]
# visit = [[0] * m for _ in range(n)]

# queue = deque([(0, 0)])
# visit[0][0] = 1
# while queue:
#     cnt = 0
#     x, y = queue.popleft()
#     if x == n-1 and y == m-1:
#         break
#     for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#         if 0 <= x+dx < n and 0 <= y+dy < m:
#             # 나아갈 수 있고(벽X) 왔던 곳이 아니고, 벽이라도 한번은 가능..
#             if visit[x+dx][y+dy] == 0:
#                 # 이미 벽 부섰음
#                 if graph[x][y] == '-1':
#                     if graph[x+dx][y+dy] == '0':
#                         graph[x+dx][y+dy] = '-1'
#                         queue.append((x+dx, y+dy))
#                         visit[x+dx][y+dy] = visit[x][y] + 1
#                     else:
#                         cnt += 1
#                 # 벽 부순 적 아직 없음
#                 else:
#                     if graph[x + dx][y + dy] == '1':
#                         graph[x+dx][y+dy] = '-1'
#                     queue.append((x+dx, y+dy))
#                     visit[x+dx][y+dy] = visit[x][y] + 1
#             else: cnt += 1
#         else:
#             cnt += 1
#         if cnt == 4:
#             break
# print(visit[n-1][m-1] if visit[n-1][m-1] else -1)


# 벽을 깬 경로와 깨지 않은 경로가 진행 도중 같은 노드에서 만났을 때 문제 발생 !!
# 둘 중에 하나가 방문체크를 하면 나머지 하나의 경로는 탐색을 더하지 못하게 됨,,
# ------> 노드가 겹치면 벽을 깬 경로와 깨지 않은 경로를 구분해 주어야함

# 5 10
#   0 0 0 0 0 1 1 0 0 0
#   1 1 0 1 0 1 1 0 1 0
#   0 0 0 0 0 0 0 0 1 0
#   1 1 1 1 1 1 1 1 1 0
#   1 1 1 1 0 0 0 0 0 0


n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]

queue = deque([(0, 0, 0)])
visit[0][0][0] = 1
while queue:
    cnt = 0
    x, y, flag = queue.popleft()    # flag가 0이면 벽 부순적 없음, 1이면 벽 부숨
    if x == n-1 and y == m-1:
        break
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < n and 0 <= y+dy < m:
            # flag 상관없이 BFS 진행 (방문경험 없고 갈수 있는 길인 경우)
            if visit[x+dx][y+dy][flag] == 0 and graph[x+dx][y+dy] == '0':
                queue.append((x+dx, y+dy, flag))
                visit[x+dx][y+dy][flag] = visit[x][y][flag] + 1
            # 갈수 있는 길이 없는 경우 flag가 0이면 벽 부순다
            elif flag == 0:
                if visit[x+dx][y+dy][1] == 0 and graph[x+dx][y+dy] == '1':
                    queue.append((x+dx, y+dy, 1))
                    visit[x+dx][y+dy][1] = visit[x][y][0] + 1
# [0, 0]이면 -1, [10, 0]이면 10, [n, m]이면  min(n, m) print
ans = min(visit[n-1][m-1]) if all(cnt > 0 for cnt in visit[n-1][m-1]) else max(visit[n-1][m-1])
print(-1 if ans == 0 else ans)

