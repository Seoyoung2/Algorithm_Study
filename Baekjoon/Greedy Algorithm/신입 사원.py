# https://www.acmicpc.net/problem/1946

from sys import stdin


# 2중 for문으로 인해 시간초과가 난 코드,,
# t = int(stdin.readline())
# for _ in range(t):
#     n = int(stdin.readline())
#     S = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
#     S.sort(reverse=True)
#
#     ans = 0
#     for i in range(n):
#         pick = True
#         for j in range(i+1, n):
#             if S[i][1] > S[j][1]:
#                 # 선발 No
#                 pick = False
#                 break
#         if pick:
#             ans += 1
#     print(ans)


# 2중 for문을 빼서 시간을 단축한 코드
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    S = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    S.sort()

    tmp, ans = n+1, 0
    for score in S:
        if tmp > score[1]:
            tmp = score[1]
            ans += 1
    print(ans)