# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


from sys import stdin

n = int(stdin.readline())
graph = []
for i in range(n):
    graph.append([])
    tmp = str(stdin.readline().rstrip())
    for j in range(n):
        graph[i].append(int(tmp[j]))


def dfs(gra, cnt, ii, jj):
    #visit[i][j] = 1
    gra[ii][jj] = 0
    xy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for x, y in xy:
        if ii+x>=0 and ii+x<n and jj+y>=0 and jj+y<n:
            # if gra[ii + x][jj + y] == 1 and visit[ii + x][jj + y] == 0:
            if gra[ii + x][jj + y] == 1:
                cnt = dfs(gra, cnt+1, ii+x, jj+y)
    return cnt


#visit = [[0] * n for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        # if graph[i][j]==1 and visit[i][j]==0:
        if graph[i][j]==1:
            ans.append(dfs(graph, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)


# DFS 와 재귀를 사용했다.
# 이차원배열 2개(graph와 visit)을 사용하다가 번지수는 이미 return값으로 나오니까 visit을 없애고 방문한 곳은 graph값을 0으로 초기화시켰다.
# ====> 메모리는 그대로고 시간 조금 줄었다.
