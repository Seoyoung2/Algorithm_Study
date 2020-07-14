# https://www.acmicpc.net/problem/1987
# 매우매우 어려웠음

# alpha를 set, list로 정의한 후 not in 으로 visit check 했더니 시간초과,,
# alpha를 26칸의 list('A'~'Z')로 정의한 후, 0/1로 visit check !!
#       + 처음 입력받을 때, map()을 이용해 알파벳을 ord()-65를 수행해서 리스트에 저장해야함

from sys import stdin

r, c = map(int, stdin.readline().split())
board = [list(map(lambda x: ord(x)-65, stdin.readline().rstrip())) for _ in range(r)]
alpha = [0] * 26


def dfs(x, y, cnt):
    global res
    if cnt > res:   res = cnt
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x + dx < r and 0 <= y + dy < c:
            if not alpha[board[x + dx][y + dy]]:
                alpha[board[x+dx][y+dy]] = 1
                dfs(x+dx, y+dy, cnt+1)
                alpha[board[x+dx][y+dy]] = 0


res = 1
alpha[board[0][0]] = 1
dfs(0, 0, 1)

print(res)
