# https://www.acmicpc.net/problem/1707

from sys import stdin


def bfs(i, graph, visit):
    queue = [i]
    visit[i] = 1
    while queue:
        node = queue.pop(0)
        for x in graph[node]:
            if visit[x] == 0:
                queue.append(x)
                visit[x] = 3 - visit[node]
            elif visit[node] == visit[x]:
                return False
    return True


k = int(stdin.readline())
for _ in range(k):
    flag = True
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]     # 1 또는 2 저장
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v+1):
        if visit[i] == 0:
            if not bfs(i, graph, visit):
                flag = False
    if flag:
        print('YES')
    else:
        print('NO')



