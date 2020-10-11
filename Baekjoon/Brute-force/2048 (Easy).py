# https://www.acmicpc.net/problem/12100
from copy import deepcopy
from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]


def move(box, flag):
    check = [[True] * N for _ in range(N)]
    if flag == 0:                       # UP
        for j in range(N):
            for i in range(N):
                if box[i][j]:
                    while 0 <= i-1 < N:
                        # 같은 숫자일 경우 -> 수 합침
                        if box[i-1][j] == box[i][j] and check[i][j] and check[i-1][j]:
                            box[i-1][j] *= 2
                            box[i][j] = 0
                            check[i-1][j] = False
                            break
                        # 다른숫자 만날 때까지 이동
                        elif box[i-1][j] == 0:
                            box[i-1][j] = box[i][j]
                            box[i][j] = 0
                        i -= 1
    elif flag == 1:                     # DOWN
        for j in range(N):
            for i in range(N-1, -1, -1):
                if box[i][j]:
                    while 0 <= i + 1 < N:
                        if box[i+1][j] == box[i][j] and check[i][j] and check[i+1][j]:
                            box[i+1][j] *= 2
                            box[i][j] = 0
                            check[i+1][j] = False
                            break
                        elif box[i+1][j] == 0:
                            box[i+1][j] = box[i][j]
                            box[i][j] = 0
                        i += 1
    elif flag == 2:                     # RIGHT
        for i in range(N):
            for j in range(N-1, -1, -1):
                if box[i][j]:
                    while 0 <= j + 1 < N:
                        if box[i][j+1] == box[i][j] and check[i][j] and check[i][j+1]:
                            box[i][j+1] *= 2
                            box[i][j] = 0
                            check[i][j+1] = False
                            break
                        elif box[i][j+1] == 0:
                            box[i][j+1] = box[i][j]
                            box[i][j] = 0
                        j += 1
    elif flag == 3:                     # LEFT
        for i in range(N):
            for j in range(N):
                if box[i][j]:
                    while 0 <= j-1 < N:
                        if box[i][j-1] == box[i][j] and check[i][j] and check[i][j-1]:
                            box[i][j-1] *= 2
                            box[i][j] = 0
                            check[i][j-1] = False
                            break
                        elif box[i][j-1] == 0:
                            box[i][j-1] = box[i][j]
                            box[i][j] = 0
                        j -= 1
    return box


# def move(a, flag):
#     check = [[True] * N for _ in range(N)]
#     if flag == 0:  # UP
#         for c in range(N):
#             for r in range(N):
#                 if a[r][c] != 0:
#                     while 0 <= r-1 < N:
#                         if a[r-1][c] == a[r][c] and check[r-1][c] and check[r][c]:
#                             a[r-1][c] *= 2
#                             check[r-1][c] = False
#                             a[r][c] = 0
#                             break
#                         else:
#                             if a[r-1][c] == 0:
#                                 a[r-1][c] = a[r][c]
#                                 a[r][c] = 0
#                         r -= 1
#
#     elif flag == 1:  # DOWN
#         for c in range(N):
#             for r in range(N - 1, -1, -1):
#                 if a[r][c] != 0:
#                     while 0 <= r+1 < N:
#                         if a[r+1][c] == a[r][c] and check[r+1][c] and check[r][c]:
#                             a[r+1][c] *= 2
#                             check[r+1][c] = False
#                             a[r][c] = 0
#                             break
#                         else:
#                             if a[r+1][c] == 0:
#                                 a[r+1][c] = a[r][c]
#                                 a[r][c] = 0
#                         r += 1
#
#     elif flag == 2:  # LEFT
#         for r in range(N):
#             for c in range(N):
#                 if a[r][c] != 0:
#                     while 0 <= c-1 < N:
#                         if a[r][c] == a[r][c-1] and check[r][c-1] and check[r][c]:
#                             a[r][c-1] *= 2
#                             check[r][c-1] = False
#                             a[r][c] = 0
#                             break
#                         else:
#                             if a[r][c-1] == 0:
#                                 a[r][c-1] = a[r][c]
#                                 a[r][c] = 0
#                         c -= 1
#
#     elif flag == 3:  # RIGHT
#         for r in range(N):
#             for c in range(N - 1, -1, -1):
#                 if a[r][c] != 0:
#                     while 0 <= c+1 < N:
#                         if a[r][c] == a[r][c+1] and check[r][c+1] and check[r][c]:
#                             a[r][c+1] *= 2
#                             check[r][c+1] = False
#                             a[r][c] = 0
#                             break
#                         else:
#                             if a[r][c+1] == 0:
#                                 a[r][c+1] = a[r][c]
#                                 a[r][c] = 0
#                         c += 1
#     return a


def solve(x, tboard):
    global ans
    if x == 5:
        ans = max(ans, max(max(tb) for tb in tboard))
        return
    for di in range(4):
        solve(x+1, move(deepcopy(tboard), di))


ans = 0
solve(0, board)
print(ans)
