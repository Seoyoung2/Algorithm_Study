# https://www.acmicpc.net/problem/11724
# DFS로 풀이

from sys import stdin

n, m = map(int, stdin.readline().split())
connect = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    # 방향성이 없으니까
    connect[a][b] = 1
    connect[b][a] = 1


def dfs(x):
    visit[x] = 1
    for i in range(1, n+1):
        if not visit[i] and connect[x][i]:
            dfs(i)


# 중복 방문을 피하기 위해 (노드 한개 마다 확인하면 되기 떄문에 1차열배열로)
visit = [0] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not visit[i]:
        cnt += 1
        dfs(i)
print(cnt)
