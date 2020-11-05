# https://www.acmicpc.net/problem/1167
# 임의의 한 점 x를 선택하고, x에서 가장 먼 정점 y를 찾은 후, 다시 y에서 가장 먼 정점 z를 찾음.
# 여기서 y와 z의 거리가 트리의 지름
import sys
sys.setrecursionlimit(10**6)


def dfs(node):
    for x, n in graph[node]:
        if check[x] == 0:
            check[x] = check[node] + n
            dfs(x)


V = int(input())
# 그래프 만들기
graph = {}
for _ in range(V):
    info = list(map(int, input().split()))
    graph[info[0]] = []
    for j in range(1, len(info)-1, 2):
        graph[info[0]].append((info[j], info[j+1]))

# 트리의 지름 찾기
check = [0] * (V + 1)
dfs(1)
tmp = check.index(max(check[2:]))
check = [0] * (V + 1)
dfs(tmp)
print(max(check[:tmp] + check[tmp+1:]))
