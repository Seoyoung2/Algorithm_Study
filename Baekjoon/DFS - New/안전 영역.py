# https://www.acmicpc.net/problem/2468
# DFS로 재귀함수를 호출하는 방식으로 풀었더니 시간이 너무 오래 걸림
# ==> stack을 이용해서 재귀호출 없이 DFS로 풀었더니 훨씬 ㄱㅊ

from sys import stdin

n = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(n)]


def dfs(cx, cy, height):
    stack = [(cx, cy)]
    while stack:
        x, y = stack.pop()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if L[x+dx][y+dy] > height and not visit[x+dx][y+dy]:
                    visit[x+dx][y+dy] = 1
                    stack.append((x+dx, y+dy))


ans = 0
high = max(num for row in L for num in row)
for h in range(0, high):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] > h and not visit[i][j]:
                cnt += 1
                visit[i][j] = 1
                dfs(i, j, h)
    ans = max(ans, cnt)
print(ans)
