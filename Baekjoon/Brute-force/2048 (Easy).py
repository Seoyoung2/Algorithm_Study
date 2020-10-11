# https://www.acmicpc.net/problem/12100
from copy import deepcopy
from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]


def move(box, flag):
    global cnt
    check = [[True] * N for _ in range(N)]
    if flag == 0:                       # UP
        for j in range(N):
            for i in range(N):
                if box[i][j]:
                    while 0 <= i-1 < N:
                        # 같은 숫자일 경우 -> 수 합침
                        if box[i-1][j] == box[i][j] and check[i-1][j]:
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
                        if box[i+1][j] == box[i][j] and check[i+1][j]:
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
                        if box[i][j+1] == box[i][j] and check[i][j+1]:
                            box[i][j+1] *= 2
                            box[i][j] = 0
                            check[i][j-1] = False
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
                        if box[i][j-1] == box[i][j] and check[i][j-1]:
                            box[i][j-1] *= 2
                            box[i][j] = 0
                            check[i][j-1] = False
                            break
                        elif box[i][j-1] == 0:
                            box[i][j-1] = box[i][j]
                            box[i][j] = 0
                        j -= 1
    for row in box:
        print(row)
    print(cnt)
    cnt += 1
    return box


cnt = 0
def solve(x, tboard):
    global ans, cnt
    if x == 5:
        ans = max(ans, max(max(tb) for tb in tboard))
        return
    for di in range(4):
        dtb = deepcopy(tboard)
        solve(x+1, move(dtb, di))


ans = 0
solve(0, board)
print(ans)
