# https://www.acmicpc.net/problem/16948

from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[-1] * N for _ in range(N)]
board[r1][c1] = 0

q = deque([(r1, c1)])
while q:
    x, y = q.popleft()
    if x == r2 and y == c2:
        break
    for dx, dy in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == -1:
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))
print(board[r2][c2])