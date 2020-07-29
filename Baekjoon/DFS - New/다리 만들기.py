# https://www.acmicpc.net/problem/2146
# 어려웠던 문제,,
# 각 섬마다 번호를 붙인다 -> 섬인 구역부터 dfs를 수행해서 다른 번호가 붙은 섬이 나타나면 종료 -> 가장 짧은 경로 구한다
# 위 방법으로는 시간초과가 발생 ==> 섬 전체를 dfs를 돌지 말고, 섬 외곽 지역만 dfs 수행?

from sys import stdin

N = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = 100000
visit = [L[k][:] for k in range(N)]


# 섬마다 번호 붙이기
def assign_num(x, y, n):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        L[cx][cy] = n
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= cx+dx < N and 0 <= cy+dy < N:
                if L[cx+dx][cy+dy] == 1:
                    stack.append((cx+dx, cy+dy))


def dfs(x, y, cnt, n):
    global ans
    if cnt > ans:
        return
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        if 0 <= x+dx < N and 0 <= y+dy < N:
            if L[x+dx][y+dy] != n:
                if L[x+dx][y+dy] == 0:
                    L[x+dx][y+dy] = n
                    dfs(x+dx, y+dy, cnt+1, n)
                    L[x+dx][y+dy] = 0
                else:
                    if ans > cnt:
                        ans = cnt
                    return


# 섬마다 번호 붙이기 (2부터)
num = 1
for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            num += 1
            assign_num(i, j, num)

# 가장 짧은 다리의 길이 찾기
for i in range(N):
    for j in range(N):
        num = L[i][j]
        if num > 0:
            dfs(i, j, 0, num)

print(ans)
for row in L:
    print(row)