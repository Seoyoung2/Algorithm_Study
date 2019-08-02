# v[n][j] : n번째 층의 j번째 원소의 값
# M[n][j] : n번째 층의 j번째 원소에서의 선택된 수의 최대 함
# M[n][j] = max(M[n-1][j-1] + v[n][j], M[n-1][j] + v[n][j])

from sys import stdin

t = int(stdin.readline())
v = []
for _ in range(t):
    v.append([int(x) for x in stdin.readline().strip().split()])
#print(v)    # [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

M = v
for n in range(1, t):
    for j in range(n+1):
        if j == 0:
            M[n][j] = M[n-1][j] + v[n][j]
        elif j == n:
            M[n][j] = M[n-1][j-1] + v[n][j]
        else:
            M[n][j] = max(M[n-1][j-1] + v[n][j], M[n-1][j] + v[n][j])

print(max(M[-1]))
