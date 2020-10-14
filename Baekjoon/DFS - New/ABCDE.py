# https://www.acmicpc.net/problem/13023
# 한줄그리기가 가능한 5개가 존재하느냐

from sys import stdin

N, M = map(int, stdin.readline().split())
friends = [[] for _ in range(N)]
visit = [False] * N
ans = False
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)


def dfs(idx, cnt):
    global ans
    visit[idx] = True
    if cnt == 5:
        ans = True
        return
    for x in friends[idx]:
        if not visit[x]:
            dfs(x, cnt+1)
            visit[x] = False


for i in range(M):
    dfs(i, 1)
    visit[i] = False
    if ans: break
print(1 if ans else 0)