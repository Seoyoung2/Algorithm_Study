# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.


from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, v):
    visit = {}
    stack = [v]

    while stack:
        node = stack.pop()
        if node not in visit:
            #visit.append(node)
            visit[node] = True
            stack.extend(sorted(graph[node], reverse=True))

    return visit


def bfs(graph, v):
    visit = {}
    #queue = [v]
    queue = deque()
    queue.append(v)

    while queue:
        #node = queue.pop(0)
        node = queue.popleft()
        if node not in visit:
            #visit.append(node)
            visit[node] = True
            queue.extend(sorted(graph[node]))

    return visit


print(*dfs(graph, v))
print(*bfs(graph, v))


# 주어진 간선으로 그래프를 만드는 방법은 <인접행렬과 인접리스트> 두가지가 있다. 나는 인접리스트를 dictionary로 구현했다.
# if node not in visit 에서 visit을 list로 구현할 경우 O(n)이 소요돼서 dictionary를 이용해 해시로 구현=> O(1)
# 또한, dfs에서 stack을, bfs에서는 queue를 리스트를 이용해서 사용했는데 이렇게하면 pop(0)을 할 때 O(n)의 시간복잡도가 걸린다.
# 그래서 list 대신에 collections.deque 를 이용했다.

# 인접리스트/ queue에 list 이용/ visit에 list 이용 : 29368KB/360ms
# 인접리스트/ queue에 list 이용/ visit에 dictionary를 이용 : 29368KB/124ms
# 인접리스트/ queue에 collections.dequeue 이용/ visit에 dictionary를 이용 : 31824KB/96ms
