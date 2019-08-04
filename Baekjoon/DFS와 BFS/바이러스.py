# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.


from sys import stdin

n = int(stdin.readline())
t = int(stdin.readline())
graph = {}
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

visit = {}
stack = [1]
while stack:
    node = stack.pop()
    if node not in visit:
        visit[node] = True
        stack.extend(graph[node])

print(len(visit)-1)
