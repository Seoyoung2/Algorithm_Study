# https://www.acmicpc.net/problem/3190

from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [[0] * N for _ in range(N)]

K = int(stdin.readline())
for _ in range(K):
    x, y = map(int, stdin.readline().split())
    board[x-1][y-1] = 1

L = int(stdin.readline())
turn = deque()
for _ in range(L):
    X, C = stdin.readline().split()
    turn.append((int(X), C))


straight = [(0, 1), (0, -1), (1, 0), (-1, 0)]
right = [(1, 0), (-1, 0), (0, -1), (0, 1)]
left = [(-1, 0), (1, 0), (0, 1), (0, -1)]
go = (0, 1)

time = 0
board[0][0] = 3
road = deque([(0, 0)])
while True:
    x, y = road[-1]
    nx = x + go[0]
    ny = y + go[1]

    # 벽 또는 자기자신의 몸과 부딪히면 게임 끝
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 3:
        break

    print(nx, ny, end=" (")

    if board[nx][ny] == 0:
        # 사과 못 먹으면
        ex, ey = road.popleft()
        board[ex][ey] = 0
    road.append((nx, ny))
    board[nx][ny] = 3

    if turn and time == turn[0][0]:
        if turn[0][1] == 'L':
            go = left[straight.index(go)]
        else:
            go = right[straight.index(go)]
        turn.popleft()
    time += 1
    print(time)

print(time)