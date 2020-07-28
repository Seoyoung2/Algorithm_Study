# https://www.acmicpc.net/problem/2573

from sys import stdin

n, m = map(int, stdin.readline().split())
B = [list(map(int, stdin.readline().split())) for _ in range(n)]


def dfs(bing, x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        bing[cx][cy] = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= cx+dx <= n and 0 <= cy+dy <= m:
                if bing[cx+dx][cy+dy]:
                    stack.append((cx+dx, cy+dy))


ans = 0
while True:
    # 빙산이 나누어졌는지 확인
    B2 = [B[i][:] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if B2[i][j] > 0:
                dfs(B2, i, j)
                cnt += 1
    if cnt != 1:
        # 처음부터 1덩어리가 아니라면 0 return
        ans = 0 if cnt == 0 else ans
        break

    ans += 1
    # 배열의 각 원소에서 얼마나 decrease해야하는지 & 방문체크 용도
    dec = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if B[i][j] and dec[i][j] == 0:
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    if 0 <= i + dx <= n and 0 <= j + dy <= m:
                        if B[i+dx][j+dy] == 0:
                            dec[i][j] += 1
    # 빙산높이에서 dec배열에 저장된 숫자만큼 빼기
    for idx in range(n):
        B[idx] = [a - b if a > b else 0 for a, b in zip(B[idx], dec[idx])]

print(ans)