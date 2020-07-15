# https://www.acmicpc.net/problem/1707

from sys import stdin

k = int(stdin.readline())
for _ in range(k):
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = True
    visit = [-1] * (v+1)
    for i in range(1, v+1):
        if visit[i] == -1:
            visit[i] = 1
            stack = [i]
            # DFS
            while stack:
                x = stack.pop()
                for j in graph[x]:
                    if visit[j] == visit[x]:
                        ans = False
                        break
                    if visit[j] == -1:
                        visit[j] = 1 - visit[x]
                        stack.append(j)
                if not ans: break
    print("YES") if ans else print("NO")
