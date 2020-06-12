# https://www.acmicpc.net/problem/7562

from sys import stdin
from collections import deque

t = int(stdin.readline())
dxdy = (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)
for _ in range(t):
    l = int(stdin.readline())
    board = [[0]*l for _ in range(l)]
    queue = deque([tuple(map(int, stdin.readline().split()))])
    goal_x, goal_y = map(int, stdin.readline().split())
    while True:
        x, y = queue.popleft()
        if x == goal_x and y == goal_y:
            break
        for dx, dy in dxdy:
            if 0 <= x + dx < l and 0 <= y + dy < l:
                if board[x+dx][y+dy] == 0 or board[x+dx][y+dy] > board[x][y] + 1:
                    board[x+dx][y+dy] = board[x][y] + 1
                    queue.append((x+dx, y+dy))

    print(board[goal_x][goal_y])