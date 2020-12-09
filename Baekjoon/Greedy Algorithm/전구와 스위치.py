# https://www.acmicpc.net/problem/2138
# 모든 경우의 수를 다 해보면서 목적 전구와 동일하면 break 했지만 메모리초과
# -> 1번 전구부터 마지막 전구까지 앞 전구를 목적 전구와 비교하면서 스위칭

import math
import sys
sys.setrecursionlimit(10**6)


def pushing(s, idx):
    s[idx] = str(1 - int(s[idx]))
    if idx != 0:
        s[idx-1] = str(1 - int(s[idx-1]))
    if idx != N-1:
        s[idx+1] = str(1 - int(s[idx+1]))


def solve(s, idx, cnt):
    global ans
    if idx == N:
        if s == goal:
            ans = min(ans, cnt)
        return
    if s[idx-1] == goal[idx-1]:
        # 현재 스위치 누르지 말기
        solve(s, idx+1, cnt)
    else:
        # 현재 스위치 누르기
        pushing(s, idx)
        solve(s, idx+1, cnt+1)


N = int(input())
cur1 = list(input())
goal = list(input())
cur2 = cur1[:]
ans = math.inf

# 첫번째 전구 off 시작
solve(cur1, 1, 0)

# 첫번째 전구 on 시작
pushing(cur2, 0)
solve(cur2, 1, 1)

print(ans if ans != math.inf else -1)