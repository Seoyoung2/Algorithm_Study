# https://www.acmicpc.net/problem/3085
# 교환한 사탕과 무관한 사탕들을 먹을 수 있음

from sys import stdin

N = int(stdin.readline())
board = [list(stdin.readline().rstrip()) for _ in range(N)]


def check_len(box):
    res = 0
    for i in range(N):
        k, l = 1, 1
        # 가로로 사탕 세기
        for j in range(1, N):
            if box[i][j] == box[i][j-1]:
                k += 1
            else:
                res = max(res, k)
                k = 1
        # 세로로 사탕 세기
        for j in range(1, N):
            if box[j][i] == box[j-1][i]:
                l += 1
            else:
                res = max(res, l)
                l = 1
        res = max(k, l, res)
    return res


ans = check_len(board)
for x in range(N):
    for y in range(N):
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if board[x][y] != board[x+dx][y+dy]:
                    board[x][y], board[x+dx][y+dy] = board[x+dx][y+dy], board[x][y]
                    ans = max(ans, check_len(board))
                    board[x][y], board[x+dx][y+dy] = board[x+dx][y+dy], board[x][y]
print(ans)
