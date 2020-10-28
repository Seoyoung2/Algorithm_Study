# https://www.acmicpc.net/problem/1261

from collections import deque


def bfs():
    q = deque([(0, 0)])
    check[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return check[x][y]
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                if miro[nx][ny] == 0:
                    q.appendleft((nx, ny))
                    check[nx][ny] = check[x][y]
                else:
                    # 벽 뚫음
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1


M, N = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(N)]
check = [[-1] * M for _ in range(N)]    # 방문 체크 + 벽을 뚫은 횟수

print(bfs())
