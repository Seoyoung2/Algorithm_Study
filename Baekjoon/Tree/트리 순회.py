# https://www.acmicpc.net/problem/1991

class Node:
    def __init__(self, root, left, right):
        self.data = root
        self.left = left
        self.right = right


def pre_order(node):
    if node == '.':
        return
    print(node.data, end="")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node == '.':
        return
    in_order(node.left)
    print(node.data, end="")
    in_order(node.right)


def post_order(node):
    if node == '.':
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end="")


N = int(input())
nodes = []
for _ in range(N):
    a, b, c = input().split()
    new_node = Node(a, b, c)
    for node in nodes:
        if a == node.left:
            node.left = new_node
            break
        elif a == node.right:
            node.right = new_node
            break
    nodes.append(new_node)

pre_order(nodes[0])
print()
in_order(nodes[0])
print()
post_order(nodes[0])
