# https://www.acmicpc.net/problem/14499

from sys import stdin

N, M, x, y, K = map(int, stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(N)]
order = list(map(int, stdin.readline().split()))


def copy_num():
    if nums[x][y]:
        # 칸수가 바닥수로 복사, 칸 == 0
        dice[5] = nums[x][y]
        nums[x][y] = 0
    else:
        # 바닥수가 칸으로 복사
        nums[x][y] = dice[5]


dice = [0] * 6
dice[5] = nums[x][y]
for o in order:
    if o == 1 and y+1 < M:      # 동쪽
        y += 1
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        copy_num()
    elif o == 2 and y-1 >= 0:    # 서쪽
        y -= 1
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        copy_num()
    elif o == 3 and x-1 >= 0:    # 북쪽
        x -= 1
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        copy_num()
    elif o == 4 and x+1 < N:     # 남쪽
        x += 1
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        copy_num()
    else:
        continue
    print(dice[0])
