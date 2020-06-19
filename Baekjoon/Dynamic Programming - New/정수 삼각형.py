# https://www.acmicpc.net/problem/1932

from sys import stdin

n = int(stdin.readline())
tree = [[0, 0]]
for i in range(1, n+1):
    tree.append([0] + list(map(int, stdin.readline().split())) + [0])
    for j in range(1, len(tree[i])-1):
        tree[i][j] += max(tree[i-1][j-1], tree[i-1][j])
print(max(tree[-1]))

