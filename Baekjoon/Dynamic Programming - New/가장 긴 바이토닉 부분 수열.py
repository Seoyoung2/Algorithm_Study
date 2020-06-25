# https://www.acmicpc.net/problem/11054
# up[i] : i를 포함한 증가하는 최대길이 / down[i] : i를 포함한 감소하는 최대길이
# up = [1,2,2,1,3,3,4,5,2,1]  down = [1,5,2,1,4,3,3,3,2,1]
# up은 앞에서부터, down은 뒤에서부터 순환

from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
up, down = [1]*n, [1]*n
for i in range(n):
    for j in range(i):
        if L[i] > L[j] and up[i] < up[j] + 1:
            up[i] = up[j] + 1
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if L[i] > L[j] and down[i] < down[j] + 1:
            down[i] = down[j] + 1
print(max([a+b for a, b in zip(up, down)]) - 1)