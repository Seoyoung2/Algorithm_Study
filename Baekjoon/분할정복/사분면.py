# https://www.acmicpc.net/problem/1891

from math import pow
import sys
sys.setrecursionlimit(10**6)

d, n = input().split()
dx, dy = map(int, input().split())

# 2차원 리스트를 다 채운 후, 이동한 칸의 값 구하기 => 메모리초과 인 듯
# l = int(pow(2, d))
# graph = [[''] * l for _ in range(l)]
#
#
# def fill_graph(x, y, n):
#     n2 = n // 2
#     for i in range(x, x+n2):
#         for j in range(y, y+n2):
#             graph[i][j] += '2'
#             graph[i][n2+j] += '1'
#             graph[n2+i][j] += '3'
#             graph[n2+i][n2+j] += '4'
#     if n2 != 1:
#         fill_graph(x, y, n2)
#         fill_graph(x, y+n2, n2)
#         fill_graph(x+n2, y, n2)
#         fill_graph(x+n2, y+n2, n2)
#
#
# fill_graph(0, 0, l)
# xy = [(i,j) for i in range(l) for j in range(l) if graph[i][j]==str(n)][0]
# print(graph[xy[0]-dy][xy[1]+dx] if 0 <= xy[0]-dy < l and 0 <= xy[1]+dx < l else -1)


# 주어진 값의 좌표(x, y)를 구한 후, 이동한 좌표의 값 구하기
def find_xy(x, y, idx, len):
    len2 = len // 2
    if idx == int(d):
        return x, y
    if n[idx] == '1':
        return find_xy(x, y+len2, idx+1, len2)
    elif n[idx] == '2':
        return find_xy(x, y, idx+1, len2)
    elif n[idx] == '3':
        return find_xy(x+len2, y, idx+1, len2)
    else:
        return find_xy(x+len2, y+len2, idx+1, len2)


def find_num(x, y, len):
    global dest_x, dest_y, res
    len2 = len // 2
    if len2 == 0:
        return
    if x <= dest_x < x+len2:
        if y <= dest_y < y+len2:
            res += '2'
            find_num(x, y, len2)
        else:
            res += '1'
            find_num(x, y+len2, len2)
    else:
        if y <= dest_y < y+len2:
            res += '3'
            find_num(x+len2, y, len2)
        else:
            res += '4'
            find_num(x+len2, y+len2, len2)


res = ""
l = pow(2, int(d))
gx, gy = find_xy(0, 0, 0, l)
dest_x, dest_y = gx-dy, gy+dx
if 0 <= dest_x < l and 0 <= dest_y < l:
    find_num(0, 0, l)
    print(res)
else:
    print(-1)