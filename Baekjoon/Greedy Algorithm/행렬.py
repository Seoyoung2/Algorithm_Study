# https://www.acmicpc.net/problem/1080

from sys import stdin

n, m = map(int, stdin.readline().split())
A = [list(stdin.readline().rstrip()) for _ in range(n)]
B = [list(stdin.readline().rstrip()) for _ in range(n)]


def convert(x, y):
    for a in range(x, x+3):
        for b in range(y, y+3):
            A[a][b] = '0' if A[a][b] == '1' else '1'
    return True if A == B else False


check = False
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            if convert(i, j):
                print(cnt)
                exit()
print(0 if A == B else -1)
