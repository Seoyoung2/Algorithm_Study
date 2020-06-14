# https://www.acmicpc.net/problem/13460

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red = [i, j]
        elif graph[i][j] == 'B':
            blue = [i, j]
        elif graph[i][j] == 'O':
            goal = [i, j]
print(blue, red, goal)

# 전혀 모르겠음........ 넘나 복잡.............다음에 다시 도전.
