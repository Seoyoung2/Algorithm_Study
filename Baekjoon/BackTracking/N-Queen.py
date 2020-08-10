# https://www.acmicpc.net/problem/9663
# 1차원 리스트를 사용하여, 인덱스 번호를 체스판의 행 번호 / 각 인덱스의 value를 열 번호로 생각
# 처음에는 순열을 사용하여 각 행마다의 퀸의 위치를 지정하고 가능한지 확인하는 방법 썼더니 시간초과,
# 두번째는 백트래킹을 이용했지만 시간초과..?
# 마지막은 두번째와 마찬가지로 백트래킹을 이용했고 문제는 math.fabs()를 사용한 것 이었음.. abs()라는 내장함수 있었음

from sys import stdin

# N = int(stdin.readline())
# ans = 0
# for board in permutations(range(N)):
#     tmp = [set(), set()]
#     for i in range(N):
#         if i-board[i] in tmp[0] or i+board[i] in tmp[1]:
#             break
#         else:
#             tmp[0].add(i-board[i])
#             tmp[1].add(i+board[i])
#     else:
#         ans += 1
# print(ans)

N = int(stdin.readline())
ans = 0
board = [-1] * N


def promising(cdx):
    for j in range(cdx):
        if board[cdx] == board[j] or cdx - j == abs(board[cdx] - board[j]):
            return False
    return True


def put_queen(cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        board[cnt] = i
        if promising(cnt):
            put_queen(cnt+1)


put_queen(0)
print(ans)