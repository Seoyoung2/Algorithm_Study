# https://www.acmicpc.net/problem/2250
# 중위순회 순서가 "열", 트리의 레벨이 "행"

import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.parent = 0


def find_root(tnode):
    while tnode.parent:
        tnode = nodes[tnode.parent]
    return tnode


def in_order(node, l):
    global order, depth
    depth = max(depth, l)  # 최대 깊이 구하기
    if node.left != -1:
        in_order(nodes[node.left], l+1)
    min_res[l] = min(min_res[l], order)
    max_res[l] = max(max_res[l], order)
    order += 1
    if node.right != -1:
        in_order(nodes[node.right], l+1)


N = int(input())
nodes = {}
for i in range(1, N+1):
    nodes[i] = Node(-1, -1)
for _ in range(N):
    a, b, c = map(int, input().split())
    nodes[a].left, nodes[a].right = b, c
    if b != -1:
        nodes[b].parent = a
    if c != -1:
        nodes[c].parent = a

order, depth = 1, 1
max_res = [0] * (N+1)
min_res = [10001] * (N+1)

root = find_root(nodes[1])
in_order(root, 1)

ans1, ans2 = -1, 0
for i in range(1, depth+1):
    if ans1 < max_res[i]-min_res[i]:
        ans1 = max_res[i]-min_res[i]
        ans2 = i
print(ans2, ans1+1)