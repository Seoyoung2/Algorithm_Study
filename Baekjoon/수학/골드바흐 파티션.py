# https://www.acmicpc.net/problem/17103
# 2-999998(M) 사이의 소수를 찾은 후, 답 구해야함

from sys import stdin

M = 999998
# 소수 찾는 방법
check = set(range(2, M+1))
for i in range(2, M+1):
    if i in check:
        check -= set(range(i+i, M+1, i))

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())   # 8
    ans = 0
    for num in check:           # 2 3 5 7 ...
        if num <= N - num:      # 2 3
            if N - num in check:
                ans += 1
        else:
            break
    print(ans)
