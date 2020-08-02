# https://www.acmicpc.net/problem/2146
# 어려웠던 문제,,
# 각 섬마다 번호를 붙인다 -> 섬인 구역부터 dfs를 수행해서 다른 번호가 붙은 섬이 나타나면 종료 -> 가장 짧은 경로 구한다
# 위 방법으로는 시간초과가 발생 ==> 섬 전체를 dfs를 돌지 말고, 섬 외곽 지역만 dfs 수행 (이 방법 역시 시간초과 발생..)
# ==> dfs대신 bfs로 풀었더니 이버에는 메모리초과.. ==> dist라는 배열로 방문체크했더니 성공 !!

from sys import stdin
from collections import deque

N = int(stdin.readline())
L = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = 100000


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


def get_distance(qn):
    global ans
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    for m in range(N):
        for n in range(N):
            if L[m][n] == qn:
                q.append((m, n))
                dist[m][n] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if L[x+dx][y+dy] and L[x+dx][y+dy] != qn:
                    ans = min(ans, dist[x][y])
                    return
                if not L[x+dx][y+dy] and dist[x+dx][y+dy] == -1:
                    dist[x+dx][y+dy] = dist[x][y] + 1
                    q.append((x+dx, y+dy))


# 섬마다 번호 붙이기 (2부터)
num = 1
for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            num += 1
            assign_num(i, j, num)

# 가장 짧은 다리의 길이 찾기
for k in range(2, num+1):
    get_distance(k)
print(ans)
